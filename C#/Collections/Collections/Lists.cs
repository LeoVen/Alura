using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Lists
    {
        public static void ListTest()
        {
            List<int> myList = new List<int>();

            for (var i = 0; i < 10; i++)
                myList.Add(i);

            DisplayList(myList, $"List size (count): {myList.Count}");
        }

        public static void ListFunctions()
        {
            List<int> list = new List<int>();

            for (var i = 0; i < 10; i++)
                list.Add(i);

            DisplayList(list, "Original List");

            // No changes are made
            list.ForEach(item => { item++; });
            DisplayList(list, "List after ForEach (no changes are made)");

            Console.WriteLine($"First : {list.First()}");
            Console.WriteLine($"Last  : {list.Last()}");

            Console.WriteLine($"First number divisible by 4 : {list.First( i => i % 4 == 0 && i != 0)}");
            Console.WriteLine($"Last number divisible by 4  : {list.Last(i => i % 4 == 0 && i != 0)}");

            for (var i = 0; i < 10; i++)
                list.Add(i);

            DisplayList(list, "Adding more items to the list");

            List<int> copia = list.GetRange(0, list.Count);
            DisplayList(copia, "Shallow Copy List");

            Console.WriteLine($"First index of 0 : {list.IndexOf(0)}");
            Console.WriteLine($"Last index of 0  : {list.LastIndexOf(0)}");

            Console.WriteLine($"First index of number divisible by 4 : {list.IndexOf(list.First(i => i % 4 == 0 && i != 0))}");
            Console.WriteLine($"Last index of number divisible by 4  : {list.LastIndexOf(list.Last(i => i % 4 == 0 && i != 0))}");

            Console.WriteLine($"First or default : {list.FirstOrDefault()}");
            Console.WriteLine($"Last or default  : {list.LastOrDefault()}");

            list.RemoveRange(0, list.Count);

            Console.WriteLine($"First or default (empty list) : {list.FirstOrDefault()}");
            Console.WriteLine($"Last or default  (empty list  : {list.LastOrDefault()}");

            List<int> clone = new List<int>(copia);
            DisplayList(clone, "Cloned List");

            clone.Sort();
            clone.Reverse();
            DisplayList(clone, "Sorted and Reversed List");

            Console.WriteLine($"Total Sum : {clone.Sum()}");
            Console.WriteLine($"Total Sum of every item multiplied by two : {clone.Sum(i => i * 2)}");
        }

        public static ReadOnlyCollection<int> ReadOnlyList()
        {
            List<int> list = new List<int>();

            for (var i = 0; i < 20; i++)
                list.Add(i);

            return list.AsReadOnly();
        }

        public static void DisplayList<T>(IList<T> list, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (T item in list)
                Console.Write($"{item} ");

            Console.WriteLine(" ");
        }
    }
}
