using AluraCSharp03.Carros;
using AluraCSharp03.Funcionarios;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp03
{
    class Program
    {
        static void Main(string[] args)
        {
            Funcionario f = new Funcionario("Robin", 3331231, 30000.0);

            Funcionario d = new Diretor("Batman", 8716384, 30000.0, 1000.0);

            Console.WriteLine(f.GetBonificacao());
            Console.WriteLine(d.GetBonificacao());

            Diretor d0 = new Diretor("Huff", 87185078, 20000.0, 200.0);
            Diretor d1 = new Diretor("Mann", 747445578, 10000.0, 1000.0);

            Console.WriteLine(d0.GetBonificacao());
            Console.WriteLine(d1.GetBonificacao());

            Diretor c0 = new Coordenador("Coord", 2133497613, 30000.0, 2000.0);

            Console.WriteLine(c0.GetBonificacao());

            Console.WriteLine(Diretor.TotalFuncionarios);

            Veiculo v = new Pickup("Edge", 20000.0, 60, "Rolls Royce", 8, 130.0);

            Console.WriteLine("Range: " + v.GetRange());
            Console.WriteLine("Price at year 1970 " + v.GetPriceInflation(1970));

            Console.ReadLine();
        }
    }
}
