using System;

namespace AluraCSharp01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Variables vars = new Variables();

            Console.WriteLine("Integer:" + vars.getInteger() +
                ", Double: " + vars.getDoublePrecisionFloatingPoint());

            Console.WriteLine("Attempting to round-trip a Double with 'R':");
            double initialValue = 0.6822871999174;
            string valueString = initialValue.ToString("R");
            double roundTripped = double.Parse(valueString);
            Console.WriteLine("{0:R} = {1:R}: {2}\n",
                              initialValue, roundTripped, initialValue.Equals(roundTripped));

            Console.WriteLine("Attempting to round-trip a Double with 'G17':");
            string valueString17 = initialValue.ToString("G17");
            double roundTripped17 = double.Parse(valueString17);
            Console.WriteLine("{0:R} = {1:R}: {2}\n",
                              initialValue, roundTripped17, initialValue.Equals(roundTripped17));

            bool boolean = true;
            char character = 'a';
            string sequence_of_characters = "Hello World!";
            int integer = 100;
            long long_integer = 2000000000000;
            float floating_point = 222.33f;
            double long_float = 2411134948271393133139.333312;

            Console.WriteLine(boolean);
            Console.WriteLine(character);
            Console.WriteLine(sequence_of_characters);
            Console.WriteLine(integer);
            Console.WriteLine(long_integer);
            Console.WriteLine(floating_point);
            Console.WriteLine(long_float);

            int number = 100;

            while (number > 0)
            {
                number--;
                Console.Write(number);
            }

            for (int i = 0, j = 20; i < j; i++, j--)
            {
                // Console.WriteLine("Hello " + i + "" + j);
                Console.WriteLine("Hello " + i + j);
            }

            Console.ReadLine();
        }
    }

    class Variables
    {
        int integer = 10;
        double doublePrecisionFloatingPoint = 3.1415;

        public int getInteger()
        {
            return this.integer;
        }

        public double getDoublePrecisionFloatingPoint()
        {
            return this.doublePrecisionFloatingPoint;
        }
    }

}
