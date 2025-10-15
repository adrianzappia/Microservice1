using Ocelot.DependencyInjection;
using Ocelot.Middleware;
using Ocelot.Provider.Polly;

var builder = WebApplication.CreateBuilder(args);

builder.Configuration.AddJsonFile("ocelot.json");

builder.Services.AddOcelot(builder.Configuration).AddPolly();

builder.Services.AddCors();

builder.AddServiceDefaults();

var app = builder.Build();

app.UseCors(x => x
.AllowAnyHeader()
.AllowAnyMethod()
.AllowAnyOrigin()
.SetPreflightMaxAge(TimeSpan.FromMinutes(10)));

app.MapGet("/", () => "Hello World!");

await app.UseOcelot();

await app.RunAsync();