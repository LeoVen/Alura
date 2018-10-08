using System;

namespace AluraCSharp02
{
    class MyClass
    {
        public string name;
        public int age;
        public double money;

        public void Represent()
        {
            Console.WriteLine(this.name + " " + this.age + " has " + this.money + " in bank");
        }
    }

    class Vector
    {
        public static ulong Total { get; private set; } = 0;

        private double _x, _y, _z;

        public Vector() { }

        public Vector(double x, double y, double z)
        {
            this._x = x;
            this._y = y;
            this._z = z;

            Total++;
        }

        public override string ToString()
        {
            return "[ " + this.X + ", " + this.Y + ", " + this.Z + " ]";
        }

        public double X
        {
            get
            {
                // Insert logic here
                return this._x;
            }
            set
            {
                // Insert logic here
                this._x = value;
            }
        }

        public double Y
        {
            get
            {
                // Insert logic here
                return this._y;
            }
            set
            {
                // Insert logic here
                this._y = value;
            }
        }

        public double Z
        {
            get
            {
                // Insert logic here
                return this._z;
            }
            set
            {
                // Insert logic here
                this._z = value;
            }
        }

        public static Vector operator + (Vector v1, Vector v2)
        {
            Vector v = new Vector
            {
                X = v1.X + v2.X,
                Y = v1.Y + v2.Y,
                Z = v1.Z + v2.Z
            };

            return v;
        }

        public static Vector operator - (Vector v1, Vector v2)
        {
            Vector v = new Vector
            {
                X = v1.X - v2.X,
                Y = v1.Y - v2.Y,
                Z = v1.Z - v2.Z
            };

            return v;
        }
    }

    class Person
    {
        public int Age { get; set; }

        public ulong CPF { get; set; }

        public ulong RG { get; set; }
    }
}
