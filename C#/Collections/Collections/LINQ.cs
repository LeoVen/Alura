using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class LINQ
    {
        public static void Test01()
        {
            List<Month> months = new List<Month>()
            {
                new Month("January", 31),
                new Month("February", 28),
                new Month("March", 31),
                new Month("April", 30),
                new Month("May", 31),
                new Month("June", 30),
                new Month("July", 31),
                new Month("August", 31),
                new Month("September", 30),
                new Month("October", 31),
                new Month("November", 30),
                new Month("December", 31)
            };

            IEnumerable<string> query0 = months
                .Where(m => m.Days == 31)
                .OrderBy(m => m.Name)
                .Select(m => m.Name.ToUpper());

            foreach (var item in query0)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query1 = months.Take(3);

            foreach (var item in query1)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query2 = months.Skip(3);

            foreach (var item in query2)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query3 = months
                .Skip(6)
                .Take(3);

            foreach (var item in query3)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query4 = months
                .TakeWhile(m => ! m.Name.ToUpper().StartsWith("S"));

            foreach (var item in query4)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query5 = months
                .SkipWhile(m => !m.Name.ToUpper().StartsWith("S"));

            foreach (var item in query5)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();
        }

        public static void Test02()
        {
            string[] seq1 = { "janeiro", "fevereiro", "março" };
            string[] seq2 = { "fevereiro", "MARÇO", "abril" };

            var query0 = seq1.Concat(seq2);

            foreach (var item in query0)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query1 = seq1.Union(seq2);

            foreach (var item in query1)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query2 = seq1.Union(seq2, StringComparer.InvariantCultureIgnoreCase);

            foreach (var item in query2)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query3 = seq1.Intersect(seq2, StringComparer.InvariantCultureIgnoreCase);

            foreach (var item in query3)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            var query4 = seq1.Except(seq2, StringComparer.InvariantCultureIgnoreCase);

            foreach (var item in query4)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();
        }

        public static void Test03()
        {
            IList<string> listaMeses = new List<string>
            {
                "Janeiro", "Fevereiro", "Março",
                "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro",
                "Outubro", "Novembro", "Dezembro"
            };
            //IList<object> listaObj = listaMeses; //NAO E POSSIVEL

            string[] arrayMeses = new string[]
            {
                "Janeiro", "Fevereiro", "Março",
                "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro",
                "Outubro", "Novembro", "Dezembro"
            };

            object[] arrayObj = arrayMeses; // COVARIANCIA

            foreach (var item in arrayObj)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            IEnumerable<object> enumObj = listaMeses; // COVARIANCIA

            foreach (var item in enumObj)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();
        }
    }

    class Month
    {
        public Month(string name, int days)
        {
            Name = name;
            Days = days;
        }

        public string Name { get; private set; }
        public int Days { get; private set; }

        public override string ToString()
        {
            return $"{Name} - {Days}";
        }
    }
}
