using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace NewsLocater.Models
{
    public class Category
    {
        public Category()
        {
            new HashSet<News>();
        }
        public int Id { get; set; }
        public string Name { get; set; }
        public  virtual ICollection<News> Newses { get; set; }
    }
}