using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AluraCSharp06
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = "pagina?argumento";

            Console.WriteLine(url.Substring(url.IndexOf('?') + 1));

            string byteBankURL = "http://www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar";

            ParamExtractor ext = new ParamExtractor(byteBankURL);

            Console.WriteLine("Value: " + ext.GetValue("moedaDestino"));

            Queue<Int64> queue = new Queue<Int64>();

            Int64 sum = 0;

            for (Int64 i = 0; i < 1000001; i++)
            {
                queue.Enqueue(i);
            }

            foreach (Int64 element in queue)
            {
                sum += element;
            }

            Console.WriteLine(sum);

            string pattern = @"\?.+=";

            Match result = Regex.Match(byteBankURL, pattern);

            Console.WriteLine(result.Value);

            Regex reg = new Regex(@"\d{4,5}-?\d{4}");

            string content = "93299-4300";

            Match m = reg.Match(content);

            Console.WriteLine(m.Value);

            Console.WriteLine(m.ToString());

            Console.WriteLine(reg.ToString());

            Console.WriteLine(queue.ToString());

            Console.WriteLine(ext.ToString());



            Derived d = new Derived();

            // If cast of wrong type, result is null
            Base b = d as Base;

            if (b != null)
            {
                Console.WriteLine(b.ToString());
            }

            Console.ReadLine();
        }
    }

    class Base
    {
        public override string ToString()
        {
            return "Base";
        }
    }
    class Derived : Base
    { }
}
