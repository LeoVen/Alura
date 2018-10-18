using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ByteBank.Modelos;
using ByteBank.Modelos.Funcionarios;
using Humanizer;

namespace AluraCSharp05
{
    class Program
    {
        static void Main(string[] args)
        {
            ContaCorrente conta = new ContaCorrente(100, 3133);

            Funcionario designer = new Designer("98713698513");

            Console.WriteLine(conta.Numero);

            Console.WriteLine(designer.CPF);

            OutraClasseTeste c = new OutraClasseTeste();

            Console.WriteLine(c.getProtected());
            Console.WriteLine(c.getProtectedInternal());

            ContaCorrente cc = new ContaCorrente(399, 22210332);


            DateTime date = new DateTime(2018, 8, 17);

            Console.WriteLine(date);

            DateTime now = DateTime.Now;

            Console.WriteLine(now);

            TimeSpan diff = now - date;

            Console.WriteLine(diff);

            TimeSpan diferenca = TimeSpan.FromSeconds(value: 3600);

            string message = "Vencimento em " + TimeSpanHumanizeExtensions.Humanize(diferenca);

            Console.WriteLine(message);

            Console.ReadLine();
        }
    }

    class OutraClasseTeste : ClasseTeste
    {
        public int getProtected()
        {
            return VariavelProtegida;
        }

        public int getProtectedInternal()
        {
            return VariavelProtegidaInterna;
        }
    }
}
