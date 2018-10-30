using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Stacks
    {
        public static void StackTest()
        {
            Stack<int> stack = new Stack<int>();

            for (var i = 0; i < 20; i++)
                stack.Push(i);
            
            DisplayStack(stack, "stack");
            Console.WriteLine($"Top element: {stack.Peek()}");

            Console.WriteLine("Removing Order:");

            while (stack.Count > 0)
            {
                Console.Write($"{stack.Pop()} ");
            }

            Console.WriteLine(" ");
        }

        public static void DisplayStack<T>(Stack<T> stack, string phrase)
        {
            Console.WriteLine(phrase);

            foreach (T item in stack)
                Console.Write($"{item} ");

            Console.WriteLine(" ");
        }
    }
}
