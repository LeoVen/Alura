using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class SortedDictionaries
    {
        public static void SortedDictionaryTest()
        {
            SortedList<string, string> sortedDict = new SortedList<string, string>();

            sortedDict.Add("avocado", "a pear-shaped fruit with a rough leathery skin, smooth oily edible flesh, and a large stone.");
            sortedDict.Add("pie", "a baked dish of fruit, or meat and vegetables, typically with a top and base of pastry.");
            sortedDict.Add("knapsack", "a bag with shoulder straps, carried on the back, and typically made of canvas or other weatherproof material.");
            sortedDict.Add("indestructible", "not able to be destroyed.");
            sortedDict.Add("multiply", "obtain from (a number) another that contains the first number a specified number of times.");

            DisplaySortedDictionary(sortedDict, "Sorted List");
        }

        public static void DisplaySortedDictionary<K, V>(IDictionary<K, V> dict, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (KeyValuePair<K, V> item in dict)
                Console.Write(string.Format("Key: {0,-15}\tValue: {1,-15}\n", item.Key, item.Value));

            Console.WriteLine(" ");
        }
    }
}
