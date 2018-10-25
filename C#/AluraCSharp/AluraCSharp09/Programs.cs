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
        static void FileStreams0()
        {
            var filePath = "./contas.txt";

            FileStream fileStream = new FileStream(filePath, FileMode.Open);

            var buffer = new byte[1024];

            var bytesRead = -1;

            while (bytesRead != 0)
            {
                bytesRead = fileStream.Read(buffer, 0, buffer.Length);

                WriteBuffer(buffer, bytesRead);
            }

            fileStream.Close();
        }

        static void FileStreams1()
        {
            var filePath = "./contas.txt";

            var buffer = new byte[1024];
            var bytesRead = -1;

            using (FileStream fileStream = new FileStream(filePath, FileMode.Open))
            {
                while (bytesRead != 0)
                {
                    bytesRead = fileStream.Read(buffer, 0, buffer.Length);

                    WriteBuffer(buffer, bytesRead);
                }
            }
        }

        static List<ContaCorrente> FileStreams2()
        {
            var filePath = "./contas.txt";

            var list = new List<ContaCorrente>();

            using (var fileStream = new FileStream(filePath, FileMode.Open))
            using (var reader = new StreamReader(fileStream, Encoding.UTF8))
            {
                while (!reader.EndOfStream)
                {
                    string row = reader.ReadLine();

                    var conta = StringToContaCorrente(row);

                    Console.WriteLine($"Conta numero: {conta.Numero},\tAgencia: {conta.Agencia},\tSaldo: {conta.Saldo.ToString().Replace(',', '.')},\tTitular: {conta.Titular.Nome}");

                    list.Add(conta);
                }
            }

            return list;
        }

        static void FileStreams3(List<ContaCorrente> list)
        {
            var filePath = "./ccontas.csv";

            using (var fileStream = new FileStream(filePath, FileMode.Create))
            {
                foreach (var item in list)
                {
                    var row = ContaCorrenteToStringCSV(item);

                    var encoding = Encoding.UTF8;

                    var bytes = encoding.GetBytes(row);

                    fileStream.Write(bytes, 0, bytes.Length);
                }
            }
        }

        static void FileStreams4(List<ContaCorrente> list)
        {
            var filePath = "./ccontas.csv";

            using (var fileStream = new FileStream(filePath, FileMode.Create))
            using (var writer = new StreamWriter(fileStream, Encoding.UTF8))
            {
                foreach (var item in list)
                {
                    writer.Write(ContaCorrenteToStringCSV(item));
                }
            }
        }

        static void FileStreams5()
        {
            var filePath = "./lines.txt";

            using (var fileStream = new FileStream(filePath, FileMode.Create))
            using (var writer = new StreamWriter(fileStream, Encoding.UTF8))
            {
                for (var i = 0; i < 10; i++)
                {
                    writer.WriteLine($"Line {i}");

                    writer.Flush(); // Escreve os dados na Stream e limpa o buffer 

                    Console.WriteLine($"'Line {i}' was written in the file. Press enter to add another line.");
                    Console.ReadLine();
                }
            }
        }

        static void FileStreams6(List<ContaCorrente> list)
        {
            var filePath = "./ccontas_bin.txt";

            using (var fileStream = new FileStream(filePath, FileMode.Create))
            using (var writer = new BinaryWriter(fileStream))
            {
                foreach (var item in list)
                {
                    writer.Write(item.Agencia);
                    writer.Write(item.Numero);
                    writer.Write(item.Saldo);
                    writer.Write(item.Titular.Nome);
                }
            }
        }

        static void FileStreams7()
        {
            var filePath = "./ccontas_bin.txt";

            using (var fileStream = new FileStream(filePath, FileMode.Open))
            using (var reader = new BinaryReader(fileStream))
            {
                while (reader.BaseStream.Position != reader.BaseStream.Length)
                {
                    var numero = reader.ReadInt32();
                    var agencia = reader.ReadInt32();
                    var saldo = reader.ReadDouble();
                    var nome = reader.ReadString();

                    Console.WriteLine($"Conta numero: {numero},\tAgencia: {agencia},\tSaldo: {saldo.ToString().Replace(',', '.')},\tTitular: {nome}");
                }
            }
        }

        static void FileStreams8()
        {
            using (var inputStream = Console.OpenStandardInput())
            using (var fileStream = new FileStream("./console_input.txt", FileMode.Create))
            {
                var buffer = new byte[1024];

                for (var i = 0; i < 4; i++)
                {                    
                    var readBytes = inputStream.Read(buffer, 0, 1024);

                    fileStream.Write(buffer, 0, readBytes);

                    fileStream.Flush();

                    Console.WriteLine($"Read bytes: {readBytes}");
                }
                
            }
        }

        static void FileStreams9()
        {
            var lines = File.ReadAllLines("./contas.txt");

            Console.WriteLine($"A total of {lines.Length} lines were read");

            var bytes = File.ReadAllBytes("./ccontas_bin.txt");

            Console.WriteLine($"A total of {bytes.Length} bytes were read");
        }
    }
}
