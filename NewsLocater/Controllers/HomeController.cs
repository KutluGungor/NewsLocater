using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Web;
using System.Web.Mvc;
using System.Web.Script.Serialization;
using System.Web.WebSockets;
using System.Xml.Linq;
using HtmlAgilityPack;
using NewsLocater.Models;
using Newtonsoft.Json;

namespace NewsLocater.Controllers
{
    public class HomeController : Controller
    {

        ApplicationDbContext db = new ApplicationDbContext();
        private static readonly HttpClient client = new HttpClient();

        public ActionResult Index()
        {
            var news = new News();
            //var categories = db.Categories.ToList();
            //ViewBag.Categories = new SelectList(categories, "Id", "Name", news.CategoryId);
            return View(news);
        }
        

        [HttpPost]
        public ActionResult Index(News model)
        {
            ViewBag.Deneme=Deneme(model.Link);
            ModelState.Clear();
            return View();   
        }


        public class Yazi
        {
            public string content;
        }

        
        private string Deneme(string url)
        {
           
            var httpClient = new HttpClient();
            var html = httpClient.GetStringAsync(url).Result;
            var htmlDocument = new HtmlDocument();
            htmlDocument.LoadHtml(html);

            //Mynet'te site kaynağından medyanet-content class'ına sahip div alıyoruz.
            var divs = htmlDocument.DocumentNode.Descendants("div")
                .Where(node => node.GetAttributeValue("class", "")
                    .Equals("medyanet-content")).ToList();

            string txt = "";

            //Aldığımız div içerisinde ki "p" taglarını txt değişkenine aktarıyoruz.

            foreach (var div in divs)
            {
                foreach (var item in div.Descendants("p"))
                {
                    txt += item.InnerText;
                }

            }

            var obj = new Yazi
            {
                content = txt
            };
            

            WebHelper webHelper = new WebHelper();
            

            string request = JsonConvert.SerializeObject(obj);

            Uri urls = new Uri(string.Format("http://eastern-verbena-163508.appspot.com/classification"));

            string response = webHelper.Post(urls, request);

            var dene = JsonConvert.DeserializeObject<Yazi>(response);

            return dene.content.ToString();

            if (response != null)
            {
                //Handle your reponse here
            }
            else
            {
                //No Response from the server

            }


            //string dosya_yolu = @"C:\metinbelgesi.txt";
            //FileStream fs = new FileStream(dosya_yolu, FileMode.OpenOrCreate, FileAccess.Write);
            //StreamWriter writer = new StreamWriter(fs);

            //writer.WriteLine(jsonString);
            //writer.Flush();
            //writer.Close();
            //fs.Close();

        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public ActionResult Create()
        {
            var news = new News();
            var categories = db.Categories.ToList();
            ViewBag.Categories = new SelectList(categories, "Id", "Name", news.CategoryId);
            return View(news);
        }


    }
}