using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Dictionaries
    {
        public static void DictionaryTest()
        {
            Dictionary<string, string> dict = new Dictionary<string, string>();

            dict.Add("pie", "a baked dish of fruit, or meat and vegetables, typically with a top and base of pastry.");
            dict.Add("knapsack", "a bag with shoulder straps, carried on the back, and typically made of canvas or other weatherproof material.");
            dict.Add("indestructible", "not able to be destroyed.");
            dict.Add("multiply", "obtain from (a number) another that contains the first number a specified number of times.");

            string result = "";

            dict.TryGetValue("pie", out result);

            Console.WriteLine($"Result for 'pie': {result}");

            result = "";

            dict.TryGetValue("armor", out result);

            Console.WriteLine($"Result for 'armor': {result}");

            dict["knapsack"] = "A bag with shoulder straps";

            result = "";

            dict.TryGetValue("knapsack", out result);

            Console.WriteLine($"Result for 'knapsack': {result}");

            DisplayDictionary(dict, "Dictionary");
        }

        public static void DisplayDictionary<K, V>(IDictionary<K, V> dict, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (KeyValuePair<K, V> item in dict)
                Console.Write(string.Format("Key: {0,-15}\tValue: {1,-15}\n", item.Key, item.Value));

            Console.WriteLine(" ");
        }
    }
}
