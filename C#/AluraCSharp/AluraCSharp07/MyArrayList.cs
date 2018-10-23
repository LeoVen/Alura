using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp07
{
    class MyArrayList<T>
    {
        private T[] elements;
        private int size;
        private int capacity;
        private int growth;

        public int Length
        {
            get
            {
                return size;
            }
        }

        public MyArrayList()
        {
            elements = new T[16];

            capacity = 16;

            size = 0;
        }

        public MyArrayList(int initialCapacity, int growthRate)
        {
            if (initialCapacity == 0)
                throw new ArgumentException("Initial capacity must not be 0");

            if (growthRate < 2)
                throw new ArgumentException("Growth rate must be greater than 1");

            elements = new T[initialCapacity];

            capacity = initialCapacity;

            growth = growthRate;

            size = 0;
        }

        public bool Add(T element)
        {
            if (element == null)
                return false;

            elements[size] = element;

            size++;

            if (full())
                grow();

            return true;
        }

        public int AddAll(params T[] elements)
        {
            int missed = 0;

            foreach (T e in elements)
            {
                if (!Add(e))
                    missed++;
            }

            return missed;
        }

        public bool Remove(T element)
        {
            int index = -1;

            for (int i = 0; i < elements.Length; i++)
            {
                if (elements[i].Equals(element))
                {
                    index = i;

                    break;
                }
            }

            if (index < 0)
                return false;

            for (int i = index; i < size; i++)
            {
                elements[i] = elements[i + 1];
            }

            size--;

            return true;
        }

        public bool Remove(int index)
        {
            if (index < 0 || index >= size)
                throw new IndexOutOfRangeException();

            return Remove(elements[index]);
        }

        public bool full()
        {
            return size == capacity;
        }

        private void grow()
        {
            capacity *= growth;

            T[] newElements = new T[capacity];

            for (int i = 0; i < elements.Length; i++)
            {
                newElements[i] = elements[i];
            }

            elements = newElements;
        }

        public T Get(int index)
        {
            if (index >= size)
                throw new ArgumentOutOfRangeException();

            return elements[index];
        }

        public void Set(int index, T element)
        {
            if (index >= size)
                throw new ArgumentOutOfRangeException();

            elements[index] = element;
        }

        public T this[int i]
        {
            get
            {
                return Get(i);
            }
            set
            {
                Set(i, value);
            }
        }
    }
}
