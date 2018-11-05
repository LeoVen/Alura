using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class JaggedArrays
    {
        public static void JaggedArrayTest()
        {
            string[][] familias = new string[3][];

            familias[0] = new string[] { "Fred", "Wilma", "Pedrita" };
            familias[1] = new string[] { "Homer", "Marge", "Lisa", "Bart", "Maggie" };
            familias[2] = new string[] { "Florinda", "Kiko" };

            foreach (var familia in familias)
            {
                Console.WriteLine(string.Join(", ", familia));
            }
        }
    }
}
