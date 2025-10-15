using ETicaret.BasketWebAPI.Models;
using Microsoft.EntityFrameworkCore;

namespace ETicaret.BasketWebAPI.Context;

public sealed class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions options) : base(options)
    {
    }

    public DbSet<Basket> Baskets { get; set; }
}