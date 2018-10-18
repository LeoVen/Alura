using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp04
{
    class Number4Exception : EvilNumberException
    {
        public string Reason { get; private set; }

        public Number4Exception(string message) : base(message)
        {
            this.Reason = "The number 4 is read almost the same way as 'death' (in China, Japan and Korea)";
        }
    }
}
