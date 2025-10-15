using ETicaret.ProductWebAPI.Models;
using Microsoft.EntityFrameworkCore;

namespace ETicaret.ProductWebAPI.Context;

public sealed class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions options) : base(options)
    {
    }

    public DbSet<Product> Products { get; set; }
}