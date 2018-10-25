using ByteBank.Modelos;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp09
{
    partial class Program
    {
        static void Main(string[] args)
        {
            // Reading with buffers
            FileStreams0();

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Reading with buffers using 'using'
            FileStreams1();

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Reading with StreamReader
            List<ContaCorrente> list = FileStreams2();

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Writing with FileStream and Encoding
            FileStreams3(list);

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Writing with StreamWriter
            FileStreams4(list);

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Writing with StreamWriter using Flush
            FileStreams5();

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Writing with BinaryWriter
            FileStreams6(list);

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Reading with BinaryReader
            FileStreams7();

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Using Console OpenStandardInput
            FileStreams8();

            Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n");

            // Using File.ReadAllLines and File.ReadAllBytes
            FileStreams9();

            Console.ReadKey();
        }

        static void WriteBuffer(byte[] buffer, int readBytes)
        {
            //var utf7 = Encoding.UTF7;
            //var utf16 = Encoding.Unicode;
            //var utf32 = Encoding.UTF32;

            var utf8 = new UTF8Encoding();

            string text = utf8.GetString(buffer, 0, readBytes);

            Console.Write(text);
        }

        static ContaCorrente StringToContaCorrente(string row)
        {
            var fields = row.Split(',');

            var agencia = fields[0];
            var numero = fields[1];
            var saldo = fields[2].Replace('.', ',');
            var nome = fields[3];

            var titular = new Cliente();
            titular.Nome = nome;

            var result = new ContaCorrente(int.Parse(agencia), int.Parse(numero));
            result.Saldo = double.Parse(saldo);
            result.Titular = titular;

            return result;
        }

        static string ContaCorrenteToStringCSV(ContaCorrente conta)
        {
            return $"{conta.Agencia},{conta.Numero},{conta.Saldo.ToString("0.00").Replace(',', '.')},{conta.Titular.Nome}\n";
        }
    }
}
