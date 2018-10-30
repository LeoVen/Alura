﻿using System;
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
            ISet<int> set0 = new HashSet<int>();

            for (var i = 0; i < 20; i++)
                set0.Add(i);

            Console.WriteLine($"The set {(set0.Contains(8) ? "contains" : "dos not contains")} the number 8");

            ISet<int> set1 = new HashSet<int>();

            for (var i = 0; i < 10; i++)
                set1.Add(i);

            Console.WriteLine($"Is set0 a Proper Subset of set1? {set0.IsProperSubsetOf(set1)}");
            Console.WriteLine($"Is set1 a Proper Subset of set0? {set1.IsProperSubsetOf(set0)}");
            Console.WriteLine($"Is set0 a Subset of set1? {set0.IsSubsetOf(set1)}");
            Console.WriteLine($"Is set1 a Subset of set0? {set1.IsSubsetOf(set0)}");
            Console.WriteLine($"Is set0 a Proper Superset of set1? {set0.IsProperSupersetOf(set1)}");
            Console.WriteLine($"Is set1 a Proper Superset of set0? {set1.IsProperSupersetOf(set0)}");
            Console.WriteLine($"Is set0 a Superset of set1? {set0.IsSupersetOf(set1)}");
            Console.WriteLine($"Is set1 a Superset of set0? {set1.IsSupersetOf(set0)}");

            ISet<int> set2 = new HashSet<int>();

            for (var i = 10; i < 20; i++)
                set2.Add(i);

            DisplaySet(set0, "Set 0");
            DisplaySet(set1, "Set 1");
            DisplaySet(set2, "Set 2");

            set0.IntersectWith(set1);

            DisplaySet(set0, "Intersection of set0 and set1");

            set0.UnionWith(set2);

            DisplaySet(set0, "Union of set0 and set2");
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
