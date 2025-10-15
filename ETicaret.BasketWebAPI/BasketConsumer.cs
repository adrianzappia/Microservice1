using MassTransit;

namespace ETicaret.BasketWebAPI;

public sealed class BasketConsumer : IConsumer<Message>
{
    public async Task Consume(ConsumeContext<Message> context)
    {
        await Task.CompletedTask;
    }
}
