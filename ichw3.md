＃详述通用的高速缓存存储器结构及工作原理
  虽然主储存器的存取速度比外储存器快得多，但它容量有限。而高速缓存存储器的工作速度比主存的存取速度快很多，接近CPU的速度，但容量比主存小很多。

  高速缓存存储器的作用像一个缓冲池，让CPU的高速数据流经这个缓冲池，在流向较慢速但具有较大容量的主储存器。即大大提高了主存到寄存器的数据传输效能。

  图中每一层都是下一层的缓存，也就是说，层次结构的每一层都缓存来自较低一层的数据。 

  缓存存储器是分块的，数据总是以块为基本单位在每一层之间传递，块的大小只在相互传递的两层之间是相同的，并且一般是越位与底层的块大小越大，这样就弥补了底层存储器每次访问的所花销的大量的时间。

