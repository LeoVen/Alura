using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class MultiDimensionalArrays
    {
        public static void MultiDimensionalArrayTest()
        {
            //string[,] resultados = new string[3, 3]
            //{
            //    {"Alemanha", "Espanha", "Itália"},
            //    {"Argentina", "Holanda", "França"},
            //    {"Holanda", "Alemanha", "Alemanha"},
            //};

            string[,] resultados = new string[4, 3];

            resultados[0, 0] = "Alemanha";
            resultados[1, 0] = "Argentina";
            resultados[2, 0] = "Holanda";
            resultados[3, 0] = "Brasil";

            resultados[0, 1] = "Espanha";
            resultados[1, 1] = "Holanda";
            resultados[2, 1] = "Alemanha";
            resultados[3, 1] = "Uruguai";

            resultados[0, 2] = "Itália";
            resultados[1, 2] = "França";
            resultados[2, 2] = "Alemanha";
            resultados[3, 2] = "Portugal";

            foreach (var selecao in resultados)
            {
                Console.WriteLine(selecao);
            }

            Console.WriteLine();

            for (int i = 0; i <= resultados.GetUpperBound(1); i++)
            {
                int year = 2014 - i * 4;

                Console.Write(year.ToString().PadRight(12));
            }

            Console.WriteLine();

            for (int i = 0; i <= resultados.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= resultados.GetUpperBound(1); j++)
                {
                    Console.Write(resultados[i, j].PadRight(12));
                }

                Console.WriteLine();
            }
        }
    }
}
