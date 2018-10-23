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

            Console.WriteLine(" ");

            MyArrayList<MyClass> list = new MyArrayList<MyClass>(10, 2);

            for (int i = 0; i < 30; i++)
            {
                list.Add(new MyClass(i));
            }

            for (int i = 0; i < list.Length; i++)
            {
                list[i].display();
            }

            Console.WriteLine(" ");

            try
            {
                list[40].display();
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine(e.StackTrace);
            }

            list.Remove(10);
            list.Remove(10);
            list.Remove(10);

            Console.WriteLine(" ");

            for (int i = 0; i < list.Length; i++)
            {
                list[i].display();
            }

            int total = list.AddAll(myArray);

            if (total != 0)
                Console.WriteLine($"{total} values were not inserted");

            total = list.AddAll(
                new MyClass(0),
                new MyClass(1),
                new MyClass(2)
            );

            Console.WriteLine(" ");

            for (int i = 0; i < list.Length; i++)
            {
                list[i].display();
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
            Console.Write($"{myNumber} ");
        }

        public override bool Equals(object obj)
        {
            MyClass myClass = obj as MyClass;

            if (myClass == null)
                return false;

            return this.myNumber == myClass.myNumber;
        }
    }
}
