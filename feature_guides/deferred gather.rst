.. _deferred gather:

***************
Deferred Gather
***************

Deferred Gather is an optimization that prevents unnecessary chunk decompression when tables are joined. 

For example, Deferred Gather limits decompression to once for each join. It achieves this by merging cached GPU operation results with other result sets.

The run-time of a deferred gather is based on the following:

* The number of keys in the ``JOIN`` statement.
* The number of non-keys in the ``SELECT`` statement, such as the attributes or fields of a table.

Example
=========

The following example illustrates how the Deferred Gather optimization reduces extraneous compression, based on a ``SELECT`` ``JOIN`` query of table a that has 100 million rows and table a that has 1 million rows.

.. code-block::

	CREATE TABLE a (x int ,y int);
	CREATE TABLE b (x int,y int);

.. code-block::

	SELECT a.y,b.y
	FROM a
	INNER JOIN b on a.x = b.x;

The following is the output result for table a:

.. code-block::

	['column[1]_5','column[1]_9','column[1]_13']
	['column[1]_17','column[1]_21','column[1]_25','column[1]_29']
	['column[1]_33','column[1]_37','column[1]_41','column[1]_45']
	['column[1]_49','column[1]_53','column[1]_57','column[1]_61','column[1]_65']
	['column[1]_69','column[1]_73','column[1]_77','column[1]_81','column[1]_85']
	['column[1]_89','column[1]_93','column[1]_97','column[1]_101','column[1]_105']
	['column[1]_109','column[1]_113','column[1]_117','column[1]_121','column[1]_125']
	['column[1]_129','column[1]_133','column[1]_137','column[1]_141']
	['column[1]_145','column[1]_149','column[1]_153','column[1]_157']
	['column[1]_161','column[1]_165','column[1]_169','column[1]_173','column[1]_177']
	['column[1]_181','column[1]_185','column[1]_189','column[1]_193','column[1]_197']
	['column[1]_201','column[1]_205','column[1]_209','column[1]_213','column[1]_217']
	['column[1]_221','column[1]_225','column[1]_229','column[1]_233']
	['column[1]_237','column[1]_241','column[1]_245','column[1]_249']
	['column[1]_253','column[1]_257','column[1]_261','column[1]_265','column[1]_269']
	['column[1]_273','column[1]_277','column[1]_281','column[1]_285','column[1]_289']
	['column[1]_293','column[1]_297','column[1]_301','column[1]_305']
	['column[1]_309','column[1]_313','column[1]_317','column[1]_321']
	['column[1]_325','column[1]_329','column[1]_333','column[1]_337','column[1]_341']
	['column[1]_345','column[1]_349','column[1]_353','column[1]_357','column[1]_361']
	['column[1]_365','column[1]_369','column[1]_373','column[1]_377']
	['column[1]_381','column[1]_385','column[1]_389','column[1]_393']
	['column[1]_397','column[1]_401','column[1]_405','column[1]_409']
	['column[1]_413','column[1]_417','column[1]_421','column[1]_425','column[1]_429']
	['column[1]_433','column[1]_437','column[1]_441','column[1]_445','column[1]_449']
	['column[1]_453','column[1]_457','column[1]_461','column[1]_465']
	['column[1]_469','column[1]_473','column[1]_477','column[1]_481','column[1]_485']
	['column[1]_489','column[1]_493','column[1]_497','column[1]_501','column[1]_505']
	['column[1]_509','column[1]_513','column[1]_517','column[1]_521']
	['column[1]_525','column[1]_529','column[1]_533','column[1]_537']
	['column[1]_541','column[1]_545','column[1]_549','column[1]_553']
	['column[1]_557','column[1]_561','column[1]_565','column[1]_569']
	['column[1]_573','column[1]_577','column[1]_581','column[1]_585']
	['column[1]_589','column[1]_593','column[1]_597','column[1]_601','column[1]_605']
	['column[1]_609','column[1]_613','column[1]_617','column[1]_621','column[1]_625']
	['column[1]_629','column[1]_633','column[1]_637','column[1]_641','column[1]_645']
	['column[1]_649','column[1]_653','column[1]_657','column[1]_661','column[1]_665']
	['column[1]_669','column[1]_673','column[1]_677','column[1]_681','column[1]_685']
	['column[1]_689','column[1]_693','column[1]_697','column[1]_701']
	['column[1]_705','column[1]_709','column[1]_713','column[1]_717']
	['column[1]_721','column[1]_725','column[1]_729','column[1]_733']
	['column[1]_737','column[1]_741','column[1]_745','column[1]_749']
	['column[1]_753','column[1]_757','column[1]_761','column[1]_765']
	['column[1]_769','column[1]_773','column[1]_777','column[1]_781']
	['column[1]_785','column[1]_789','column[1]_793','column[1]_797']
	['column[1]_801','column[1]_805','column[1]_809','column[1]_813']
	['column[1]_817','column[1]_821','column[1]_825','column[1]_829','column[1]_833']
	['column[1]_837','column[1]_841','column[1]_845']
	
The following is the output result for table b:

.. code-block::

	['column[3]_7','column[3]_11','column[3]_15','column[3]_19','column[3]_23',
	'column[3]_27','column[3]_31','column[3]_35','column[3]_39','column[3]_43',
	'column[3]_47','column[3]_51','column[3]_55','column[3]_59','column[3]_63',
	'column[3]_67','column[3]_71','column[3]_75','column[3]_79','column[3]_83',
	'column[3]_87','column[3]_91','column[3]_95','column[3]_99','column[3]_103',
	'column[3]_107','column[3]_111','column[3]_115','column[3]_119','column[3]_123',
	'column[3]_127','column[3]_131','column[3]_135','column[3]_139','column[3]_143',
	'column[3]_147','column[3]_151','column[3]_155','column[3]_159','column[3]_163',
	'column[3]_167','column[3]_171','column[3]_175','column[3]_179','column[3]_183',
	'column[3]_187','column[3]_191','column[3]_195','column[3]_199','column[3]_203',
	'column[3]_207','column[3]_211','column[3]_215','column[3]_219','column[3]_223',
	'column[3]_227','column[3]_231','column[3]_235','column[3]_239','column[3]_243',
	'column[3]_247','column[3]_251','column[3]_255','column[3]_259','column[3]_263',
	'column[3]_267','column[3]_271','column[3]_275','column[3]_279','column[3]_283',
	'column[3]_287','column[3]_291','column[3]_295','column[3]_299','column[3]_303',
	'column[3]_307','column[3]_311','column[3]_315','column[3]_319','column[3]_323',
	'column[3]_327','column[3]_331','column[3]_335','column[3]_339','column[3]_343',
	'column[3]_347','column[3]_351','column[3]_355','column[3]_359','column[3]_363',
	'column[3]_367','column[3]_371','column[3]_375','column[3]_379','column[3]_383',
	'column[3]_387','column[3]_391','column[3]_395','column[3]_399','column[3]_403',
	'column[3]_407','column[3]_411','column[3]_415','column[3]_419','column[3]_423',
	'column[3]_427','column[3]_431','column[3]_435','column[3]_439','column[3]_443',
	'column[3]_447','column[3]_451','column[3]_455','column[3]_459','column[3]_463',
	'column[3]_467','column[3]_471','column[3]_475','column[3]_479','column[3]_483',
	'column[3]_487','column[3]_491','column[3]_495','column[3]_499','column[3]_503',
	'column[3]_507','column[3]_511','column[3]_515','column[3]_519','column[3]_523',
	'column[3]_527','column[3]_531','column[3]_535','column[3]_539','column[3]_543',
	'column[3]_547','column[3]_551','column[3]_555','column[3]_559','column[3]_563',
	'column[3]_567','column[3]_571','column[3]_575','column[3]_579','column[3]_583',
	'column[3]_587','column[3]_591','column[3]_595','column[3]_599','column[3]_603',
	'column[3]_607','column[3]_611','column[3]_615','column[3]_619','column[3]_623',
	'column[3]_627','column[3]_631','column[3]_635','column[3]_639','column[3]_643',
	'column[3]_647','column[3]_651','column[3]_655','column[3]_659','column[3]_663',
	'column[3]_667','column[3]_671','column[3]_675','column[3]_679','column[3]_683',
	'column[3]_687','column[3]_691','column[3]_695','column[3]_699','column[3]_703',
	'column[3]_707','column[3]_711','column[3]_715','column[3]_719','column[3]_723',
	'column[3]_727','column[3]_731','column[3]_735','column[3]_739','column[3]_743',
	'column[3]_747','column[3]_751','column[3]_755','column[3]_759','column[3]_763',
	'column[3]_767','column[3]_771','column[3]_775','column[3]_779','column[3]_783',
	'column[3]_787','column[3]_791','column[3]_795','column[3]_799','column[3]_803',
	'column[3]_807','column[3]_811','column[3]_815','column[3]_819','column[3]_823',
	'column[3]_827','column[3]_831','column[3]_835','column[3]_839','column[3]_843',
	'column[3]_847']
	
Joining the above tables decompresses table a 844 times and table b 211 times, including ``NULL`` and value columns for each table. Using the table in this example, the longest process was ``DeferredGather.GpuDecompress``, taking 6.7 seconds.