using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Sets
    {
        public static void SetTest()
        {
            ISet<int> mySet = new HashSet<int>();

            for (var i = 0; i < 20; i++)
                mySet.Add(i);

            DisplaySet(mySet, "Original Set");

            for (var i = 0; i < 20; i++)
                mySet.Add(i);

            DisplaySet(mySet, "When adding the same elements");
        }

        public static void SetFunctions()
        {
            
        }

        public static void DisplaySet<T>(ISet<T> set, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (T item in set)
                Console.Write($"{item} ");

            Console.WriteLine(" ");
        }
    }
}
