using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp08
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> intList = new List<int>();
            List<MyClass> myClassList = new List<MyClass>();

            intList.AddAll<int>(0, 1, 2, 3, 4);
            intList.AddAll(5, 6, 7, 8, 9);

            myClassList.AddAll(new MyClass(0), new MyClass(1), new MyClass(2));
            myClassList.AddAll(new MyClass(1), new MyClass(2), new MyClass(3));
            myClassList.AddAll(new MyClass(2), new MyClass(3), new MyClass(4));

            foreach (var item in intList)
            {
                Console.WriteLine(item);
            }

            myClassList.Sort(); // If MyClass implements IComparable

            foreach (var item in myClassList)
            {
                item.display();
            }

            Console.WriteLine(" ");
            
            myClassList.AddAll(new MyClass(0), new MyClass(1), new MyClass(2));
            myClassList.AddAll(new MyClass(1), new MyClass(2), new MyClass(3));
            myClassList.AddAll(new MyClass(2), new MyClass(3), new MyClass(4));

            myClassList.Sort(new MyClassComparer()); // A class that implements IComparer of type MyClass

            foreach (var item in myClassList)
            {
                item.display();
            }

            Console.WriteLine(" ");

            myClassList.AddAll(new MyClass(0), new MyClass(1), new MyClass(2));
            myClassList.AddAll(new MyClass(1), new MyClass(2), new MyClass(3));
            myClassList.AddAll(new MyClass(2), new MyClass(3), new MyClass(4));

            IOrderedEnumerable<MyClass> orderedCollection =  myClassList.OrderBy(x => x.MyNumber); // OderBy orders by a specified class property

            foreach (var item in orderedCollection)
            {
                item.display();
            }

            var myClass = new MyClass(99);
            
            Console.ReadKey();
        }
    }

    class MyClass : IComparable
    {
        int myNumber;

        public int MyNumber { get => myNumber; set => myNumber = value; }

        public MyClass(int number)
        {
            MyNumber = number;
        }

        public int CompareTo(object obj)
        {
            var c = obj as MyClass;

            if (c == null)
                throw new InvalidCastException();

            return this.MyNumber - c.MyNumber;
        }

        public void display()
        {
            Console.Write($"{MyNumber} ");
        }

        public override bool Equals(object obj)
        {
            MyClass myClass = obj as MyClass;

            if (myClass == null)
                return false;

            return this.MyNumber == myClass.MyNumber;
        }
    }

    class MyClassComparer : IComparer<MyClass>
    {
        public int Compare(MyClass x, MyClass y)
        {
            if (x == null || y == null)
                throw new NullReferenceException();

            return x.MyNumber - y.MyNumber;
        }
    }
}
