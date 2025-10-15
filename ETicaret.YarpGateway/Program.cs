using Microsoft.AspNetCore.RateLimiting;
using Scalar.AspNetCore;
using System.Threading.RateLimiting;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

builder.Services.AddRateLimiter(cfr =>
{
    cfr.AddFixedWindowLimiter("fixed", x =>
    {
        x.QueueLimit = 100;
        x.PermitLimit = 100;
        x.Window = TimeSpan.FromMinutes(1);
        x.QueueProcessingOrder = QueueProcessingOrder.OldestFirst;
    });
});

builder.Services.AddOpenApi();

builder.AddServiceDefaults();

var app = builder.Build();

app.MapOpenApi();
app.MapScalarApiReference();

app.MapGet("/", () =>
{
    return "Hello World!";
});

app.UseRateLimiter();

app.MapReverseProxy();

app.Run();
