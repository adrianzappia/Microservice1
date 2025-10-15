using Projects;

var builder = DistributedApplication.CreateBuilder(args);

var username = builder.AddParameter("username", "admin", secret: true);
var password = builder.AddParameter("password", "admin", secret: true);

var rmq = builder.AddRabbitMQ("rabbitMQ", username, password, 5672)
    .WithLifetime(ContainerLifetime.Persistent)
    .WithImage("rabbitmq", "3-management")
    .WithHttpEndpoint(port: 15672, targetPort: 15672, name: "management");

builder.AddProject<ETicaret_OcelotGateway>("ocelot");
builder.AddProject<ETicaret_YarpGateway>("yarp");
builder.AddProject<ETicaret_ProductWebAPI>("product").WaitFor(rmq);
builder.AddProject<ETicaret_BasketWebAPI>("basket").WaitFor(rmq);

builder.Build().Run();
