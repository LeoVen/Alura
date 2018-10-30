using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class LinkedLists
    {
        public static void LinkedListTest()
        {
            LinkedList<int> list = new LinkedList<int>();

            LinkedListNode<int> node = null;

            for (var i = 0; i < 20; i++)
            {
                if (i == 10)
                    node = list.AddLast(i);
                else
                    list.AddLast(i);
            }

            list.AddAfter(node, 99);
            list.AddBefore(node, 99);

            DisplayList(list, "List");

            for (var i = 0; i > -20; i--)
            {
                if (i == -10)
                    node = list.AddFirst(i);
                else
                    list.AddFirst(i);
            }


            list.AddAfter(node, 99);
            list.AddBefore(node, 99);

            DisplayList(list, "List");
        }

        public static void DisplayList<T>(LinkedList<T> list, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (T item in list)
                Console.Write($"{item} ");

            Console.WriteLine(" ");
        }
    }
}
