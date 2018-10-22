using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp07
{
    class Program
    {
        static void Main(string[] args)
        {
            // Array
            int[] array = new int[10];


            for (int i = 0; i < array.Length; i++)
            {
                array[i] = i;
            }

            foreach (int i in array)
            {
                Console.Write("{0} ", i);
            }

            Console.WriteLine($"Array length: {array.Length}");

            MyClass[] myArray = new MyClass[10];

            for (int i = 0; i < myArray.Length; i++)
            {
                myArray[i] = new MyClass(i);
            }

            foreach (MyClass m in myArray)
            {
                m.display();
            }

            MyClass[] anotherArray = new MyClass[]
            {
                new MyClass(0),
                new MyClass(1),
                new MyClass(2)
            };


            Console.WriteLine(" ");

            foreach (MyClass m in anotherArray)
            {
                m.display();
            }

            Console.ReadKey();
        }
    }

    class MyClass
    {
        int myNumber;

        public MyClass(int number)
        {
            myNumber = number;
        }

        public void display()
        {
            Console.WriteLine(myNumber);
        }
    }
}
