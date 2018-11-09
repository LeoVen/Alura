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

            Display("Dictionary");
            Dictionaries.DictionaryTest();

            Display("Linked List");
            LinkedLists.LinkedListTest();

            Display("Stack");
            Stacks.StackTest();

            Display("Queue");
            Queues.QueueTest();

            // Sorted by keys using a list
            Display("SortedList");
            SortedLists.SortedListTest();

            // Sorted by keys using a balanced binary tree
            Display("SortedDictionary");
            SortedDictionaries.SortedDictionaryTest();

            // Sorted set using a balanced binary tree
            Display("SortedSet");
            SortedSets.SortedSetTest();
            SortedSets.SortedSetFunctions();

            Display("Multi Dimensional Array");
            MultiDimensionalArrays.MultiDimensionalArrayTest();

            Display("JaggedArray");
            JaggedArrays.JaggedArrayTest();

            Display("LINQ");
            LINQ.Test01();
            LINQ.Test02();
            LINQ.Test03();
        }

        static void Display(string s)
        {
            Console.WriteLine("--------------------------------------------------");
            Console.WriteLine(s);
            Console.WriteLine("--------------------------------------------------");
        }
    }
}
