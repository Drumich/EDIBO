using Microsoft.EntityFrameworkCore;
using MvcSQL.Models;

namespace MvcSQL.Data
{
    public class SQLContext : DbContext
    {
        public MvcSQLContext (DbContextOptions<MvcSQLContext> options)
            : base(options)
        {
        }

        public DbSet<SQL> aaaaaaaaaaaaaaa { get; set; }
    }
}