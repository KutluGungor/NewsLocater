using System.Data.Entity;
using NewsLocater.Models;

namespace NewsLocater
{
    public class ApplicationDbContext:DbContext
    {
        public ApplicationDbContext() : base("DefaultConnection")
        {

        }

        public virtual DbSet<News> News { get; set; }
        public virtual DbSet<Category> Categories { get; set; }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            //News Builder
            modelBuilder.Entity<News>().HasKey(p => p.Id);
            modelBuilder.Entity<News>().Property(p => p.Link).IsRequired().HasMaxLength(300);
            modelBuilder.Entity<News>().Property(p => p.Text).IsRequired();
            modelBuilder.Entity<News>().HasRequired(r => r.Category).WithMany(m => m.Newses).HasForeignKey(f=>f.CategoryId);

            //Category Builder
            modelBuilder.Entity<Category>().HasKey(p => p.Id);
            modelBuilder.Entity<Category>().Property(p => p.Name).IsRequired().HasMaxLength(75);
        }
    }
    
}