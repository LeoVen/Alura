using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class SortedLists
    {
        public static void SortedListTest()
        {
            SortedList<string, string> sortedList = new SortedList<string, string>();

            sortedList.Add("avocado", "a pear-shaped fruit with a rough leathery skin, smooth oily edible flesh, and a large stone.");
            sortedList.Add("pie", "a baked dish of fruit, or meat and vegetables, typically with a top and base of pastry.");
            sortedList.Add("knapsack", "a bag with shoulder straps, carried on the back, and typically made of canvas or other weatherproof material.");
            sortedList.Add("indestructible", "not able to be destroyed.");
            sortedList.Add("multiply", "obtain from (a number) another that contains the first number a specified number of times.");

            DisplaySortedList(sortedList, "Sorted List");
        }

        public static void DisplaySortedList<K, V>(IDictionary<K, V> dict, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (KeyValuePair<K, V> item in dict)
                Console.Write(string.Format("Key: {0,-15}\tValue: {1,-15}\n", item.Key, item.Value));

            Console.WriteLine(" ");
        }
    }
}
