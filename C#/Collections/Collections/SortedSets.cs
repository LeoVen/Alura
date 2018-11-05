using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class SortedSets
    {
        public static void SortedSetTest()
        {
            ISet<int> mySet = new SortedSet<int>();

            for (var i = 0; i < 20; i++)
                mySet.Add(i);

            DisplaySortedSet(mySet, "Original Set");

            for (var i = 0; i < 20; i++)
                mySet.Add(i);

            DisplaySortedSet(mySet, "When adding the same elements");
        }

        public static void SortedSetFunctions()
        {
            ISet<int> set0 = new SortedSet<int>();

            for (var i = 19; i >= 0; i--)
                set0.Add(i);

            Console.WriteLine($"The set {(set0.Contains(8) ? "contains" : "dos not contains")} the number 8");

            ISet<int> set1 = new SortedSet<int>();

            for (var i = 9; i >= 0; i--)
                set1.Add(i);

            Console.WriteLine($"Is set0 a Proper Subset of set1? {set0.IsProperSubsetOf(set1)}");
            Console.WriteLine($"Is set1 a Proper Subset of set0? {set1.IsProperSubsetOf(set0)}");
            Console.WriteLine($"Is set0 a Subset of set1? {set0.IsSubsetOf(set1)}");
            Console.WriteLine($"Is set1 a Subset of set0? {set1.IsSubsetOf(set0)}");
            Console.WriteLine($"Is set0 a Proper Superset of set1? {set0.IsProperSupersetOf(set1)}");
            Console.WriteLine($"Is set1 a Proper Superset of set0? {set1.IsProperSupersetOf(set0)}");
            Console.WriteLine($"Is set0 a Superset of set1? {set0.IsSupersetOf(set1)}");
            Console.WriteLine($"Is set1 a Superset of set0? {set1.IsSupersetOf(set0)}");

            ISet<int> set2 = new SortedSet<int>();

            for (var i = 10; i < 20; i++)
                set2.Add(i);

            DisplaySortedSet(set0, "Set 0");
            DisplaySortedSet(set1, "Set 1");
            DisplaySortedSet(set2, "Set 2");

            set0.IntersectWith(set1);

            DisplaySortedSet(set0, "Intersection of set0 and set1");

            set0.UnionWith(set2);

            DisplaySortedSet(set0, "Union of set0 and set2");
        }

        public static void DisplaySortedSet<T>(ISet<T> set, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (T item in set)
                Console.Write($"{item} ");

            Console.WriteLine(" ");
        }
    }
}
