using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp06
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = "pagina?argumento";

            Console.WriteLine(url.Substring(url.IndexOf('?') + 1));

            Console.ReadLine();
        }
    }
}
