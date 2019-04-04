using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace NewsLocater.Models
{
    public class News
    {
        public int Id { get; set; }
        public string Link { get; set; }
        public string Text { get; set; }
        public int CategoryId { get; set; }
        public virtual Category Category { get; set; }
    }
}