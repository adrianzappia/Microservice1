using ETicaret.ProductWebAPI.Context;
using ETicaret.ProductWebAPI.Models;
using Microsoft.EntityFrameworkCore;
using Scalar.AspNetCore;
using Steeltoe.Discovery.Consul;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<ApplicationDbContext>(opt =>
{
    opt.UseInMemoryDatabase("MyDb");
});

builder.Services.AddOpenApi();

builder.Services.AddHealthChecks();

builder.Services.AddConsulDiscoveryClient();

builder.AddServiceDefaults();

var app = builder.Build();

app.MapOpenApi();

app.MapScalarApiReference();

app.MapGet(string.Empty, () =>
{
    Console.WriteLine("I am working... {0}", DateTime.Now);
    return "Hello product webapi";
});

app.MapGet("getall", async (ApplicationDbContext dbContext, CancellationToken cancellationToken) =>
{
    var products = await dbContext.Products.ToListAsync(cancellationToken);
    products.Add(new Product()
    {
        Id = Guid.Parse("2ff8bf70-e435-41ae-803c-8a765ad7193b"),
        Name = "Bilgisayar",
        Stock = 10
    });
    return products;
});

app.MapHealthChecks("health");

app.Run();