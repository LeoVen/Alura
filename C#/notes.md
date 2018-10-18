# Notes

<table>
	<thead>
		<tr>
			<th>PARA / DE</th>
			<th>byte</th>
			<th>short</th>
			<th>char</th>
			<th>int</th>
			<th>long</th>
			<th>float</th>
			<th>double</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>byte</td>
			<td>----</td>
			<td><em>Impl.</em></td>
			<td>(char)</td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
		</tr>
		<tr>
			<td>short</td>
			<td>(byte)</td>
			<td>----</td>
			<td>(char)</td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
		</tr>
		<tr>
			<td>char</td>
			<td>(byte)</td>
			<td>(short)</td>
			<td>----</td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
		</tr>
		<tr>
			<td>int</td>
			<td>(byte)</td>
			<td>(short)</td>
			<td>(char)</td>
			<td>----</td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
		</tr>
		<tr>
			<td>long</td>
			<td>(byte)</td>
			<td>(short)</td>
			<td>(char)</td>
			<td>(int)</td>
			<td>----</td>
			<td><em>Impl.</em></td>
			<td><em>Impl.</em></td>
		</tr>
		<tr>
			<td>float</td>
			<td>(byte)</td>
			<td>(short)</td>
			<td>(char)</td>
			<td>(int)</td>
			<td>(long)</td>
			<td>----</td>
			<td><em>Impl.</em></td>
		</tr>
		<tr>
			<td>double</td>
			<td>(byte)</td>
			<td>(short)</td>
			<td>(char)</td>
			<td>(int)</td>
			<td>(long)</td>
			<td>(float)</td>
			<td>----</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th>TIPO</th>
			<th>TAMANHO</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>boolean</td>
			<td>1 byte</td>
		</tr>
		<tr>
			<td>byte</td>
			<td>1 byte</td>
		</tr>
		<tr>
			<td>short</td>
			<td>2 bytes</td>
		</tr>
		<tr>
			<td>char</td>
			<td>2 bytes</td>
		</tr>
		<tr>
			<td>int</td>
			<td>4 bytes</td>
		</tr>
		<tr>
			<td>float</td>
			<td>4 bytes</td>
		</tr>
		<tr>
			<td>long</td>
			<td>8 bytes</td>
		</tr>
		<tr>
			<td>double</td>
			<td>8 bytes</td>
		</tr>
	</tbody>
</table>


# Useful links

https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/knowing-when-to-use-override-and-new-keywords