using ETicaret.BasketWebAPI;
using ETicaret.BasketWebAPI.Context;
using ETicaret.BasketWebAPI.Models;
using MassTransit;
using Microsoft.EntityFrameworkCore;
using Polly;
using Polly.Registry;
using Polly.Retry;
using Steeltoe.Common.Discovery;
using Steeltoe.Discovery.Consul;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<ApplicationDbContext>(opt =>
{
    opt.UseInMemoryDatabase("MyDb");
});
builder.Services.AddHttpClient();

builder.Services.AddConsulDiscoveryClient();

builder.Services.AddResiliencePipeline("my-pipeline", builder =>
{
    builder.AddRetry(new RetryStrategyOptions()
    {
        MaxRetryAttempts = 3,
        Delay = TimeSpan.FromSeconds(10),
    })
    .AddTimeout(TimeSpan.FromSeconds(60));
});

builder.AddServiceDefaults();

builder.Services.AddMassTransit(c =>
{
    c.AddConsumer<BasketConsumer>();

    c.UsingRabbitMq((ctx, cfg) =>
    {
        cfg.Host("localhost", "/", h => { h.Username("admin"); h.Password("admin"); });

        cfg.ReceiveEndpoint("basket-queue", e =>
        {
            e.ConfigureConsumer<BasketConsumer>(ctx);
        });
    });
});

var app = builder.Build();

app.MapGet(string.Empty, () => "Hello basket webapi");

app.MapGet("send", async (IPublishEndpoint publishEndpoint) =>
{
    await publishEndpoint.Publish(new Message("Hello world from basket webapi"));
    return "Is done";
});

app.MapGet("getall", async (
    ApplicationDbContext dbContext,
    IDiscoveryClient discoveryClient,
    ResiliencePipelineProvider<string> resiliencePipeline,
    HttpClient httpClient, CancellationToken cancellationToken) =>
{
    var baskets = await dbContext.Baskets.ToListAsync(cancellationToken);
    baskets.Add(new Basket()
    {
        ProductId = Guid.Parse("2ff8bf70-e435-41ae-803c-8a765ad7193b"),
        Quantity = 1
    });

    var pipeline = resiliencePipeline.GetPipeline("my-pipeline");

    var productWebAPIEndpoints = await pipeline.ExecuteAsync(async callback
        => await discoveryClient.GetInstancesAsync("ProductWebAPI", callback));

    var productEndpoint = productWebAPIEndpoints.First().Uri;

    var products = await pipeline.ExecuteAsync(async callback => await httpClient
        .GetFromJsonAsync<List<Product>>($"{productEndpoint}getall", callback));

    var newBaskets = baskets.Select(s => new
    {
        Id = s.Id,
        ProductId = s.ProductId,
        ProductName = products!.FirstOrDefault(i => i.Id == s.ProductId)?.Name ?? string.Empty,
        Quantity = s.Quantity,
    }).ToList();

    return newBaskets;
});

app.Run();

class Product
{
    public Guid Id { get; set; }
    public string Name { get; set; } = default!;
}
