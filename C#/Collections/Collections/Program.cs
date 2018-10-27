using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Program
    {
        static void Main(string[] args)
        {
            Display("Array");
            Arrays.ArrayTest();
            Arrays.ArrayFunctions();

            Display("List");
            Lists.ListTest();
            Lists.ListFunctions();
            // Returns a readonly collection
            IReadOnlyList<int> readOnlyList = Lists.ReadOnlyList();
            Console.WriteLine("Read Only Collection");
            foreach (int item in readOnlyList) { Console.Write($"{item} "); }
            Console.WriteLine(" ");

            Display("Set");
            Sets.SetTest();
            Sets.SetFunctions();
        }

        static void Display(string s)
        {
            Console.WriteLine("--------------------------------------------------");
            Console.WriteLine(s);
            Console.WriteLine("--------------------------------------------------");
        }
    }
}
