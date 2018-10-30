using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Queues
    {
        public static void QueueTest()
        {
            Queue<int> queue = new Queue<int>();

            for (var i = 0; i < 20; i++)
                queue.Enqueue(i);

            DisplayQueue(queue, "queue");
            Console.WriteLine($"Element at the beginning of the queue: {queue.Peek()}");

            Console.WriteLine("Removing Order:");

            while (queue.Count > 0)
            {
                Console.Write($"{queue.Dequeue()} ");
            }

            Console.WriteLine(" ");
        }

        public static void DisplayQueue<T>(Queue<T> stack, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (T item in stack)
                Console.Write($"{item} ");

            Console.WriteLine(" ");
        }
    }
}
