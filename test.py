import sys

from PySide6.QtCore import Qt, QSize, QObject, QEvent, QRect, QPoint
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QPlainTextEdit,
    QSizePolicy,
    QLayout,
)

strings = [
    """
The next message will demonstrate how the "fitted text" issue does not occur outside of the client.
    """,
    """
thisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwithoutspacesordashesthisisalongwordwit💩houtspacesordashes
    """,
    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. In a neque vitae diam blandit porttitor id in leo. Fusce varius urna a suscipit euismod. Praesent dapibus, dui vehicula accumsan ornare, augue felis maximus metus, quis faucibus magna libero id lectus. Sed lobortis vestibulum finibus. Integer dui lorem, porttitor dapibus malesuada in, vestibulum id tellus. Phasellus sollicitudin orci nunc, sed fringilla odio lobortis commodo. Duis rutrum nunc justo, sit amet dictum nulla aliquam at. Fusce non nisi mauris. Maecenas et auctor purus, lacinia elementum velit. Mauris congue est ac tortor auctor hendrerit. Fusce ac sollicitudin augue. Etiam imperdiet purus quis risus ultrices, ut iaculis ante convallis.

Fusce eros massa, laoreet nec augue nec, aliquam finibus elit. Praesent ullamcorper dignissim odio, id gravida dui sollicitudin at. Nunc eget laoreet diam. Nam vitae mauris dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mollis nibh nec dapibus egestas. Sed ut sodales dui. Cras facilisis ex quis quam maximus euismod. Vestibulum sed ullamcorper orci, nec tempor orci. Sed felis est, luctus mollis dolor eu, mattis ornare leo. Aliquam interdum ac tortor quis facilisis. Donec hendrerit ullamcorper orci vitae facilisis. Morbi odio justo, fringilla sed fermentum vitae, pellentesque eget ante. Etiam elementum tincidunt sapien in interdum. In hac habitasse platea dictumst. Suspendisse non metus non risus congue luctus.

Praesent laoreet malesuada ante eu accumsan. Phasellus quis ipsum eu purus sodales malesuada vitae ac eros. Vestibulum augue nisi, ullamcorper viverra ultricies at, semper quis felis. Sed tempus nulla arcu. Cras porta felis sit amet eros sollicitudin, at ullamcorper metus iaculis. Aliquam quis tristique ex, ac molestie libero. Morbi molestie ex est, ut maximus urna eleifend quis. Aenean dignissim, neque id lacinia tempus, nisl diam faucibus ligula, id maximus quam magna sit amet tellus. Ut hendrerit placerat tincidunt. Aenean tincidunt cursus lorem, ut sagittis lacus vestibulum sed. Nam sapien mauris, lacinia a quam convallis, iaculis scelerisque purus. Nam posuere ante et sapien scelerisque vulputate.

Donec aliquet consequat magna. Phasellus porta turpis nec nibh posuere, eget rhoncus tellus mollis. Vivamus est odio, volutpat aliquet sem pulvinar, ornare blandit libero. Nam dui nunc, tempor in commodo eget, laoreet et tellus. Aliquam tincidunt nunc tortor, id tempus lorem imperdiet at. Pellentesque euismod, nisl et pretium dignissim, nisl ante pellentesque turpis, dignissim iaculis neque massa aliquam sapien. Sed tincidunt felis metus, eu elementum felis lacinia sit amet. Nulla sagittis euismod mauris sit amet interdum. Ut in pellentesque libero, ullamcorper rutrum diam. Donec in semper ligula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi dignissim est urna, a scelerisque est sollicitudin sit amet.

Maecenas sit amet pulvinar libero. Curabitur tempus, mauris et dictum egestas, metus nunc pharetra eros, at consectetur lorem dui eu dolor. Proin lectus ex, vestibulum sed maximus vel, tempor eu metus. Curabitur ac ornare arcu. Nulla eget felis eget sem pharetra vulputate. Aenean vestibulum eros ex, sed luctus ligula posuere non. Fusce et vestibulum elit. Proin ultricies, odio at interdum tincidunt, leo nulla tincidunt sem, at tincidunt enim enim eget arcu. Etiam at arcu purus. In laoreet purus id tristique venenatis. Donec porta, felis vel vulputate fermentum, ante est laoreet velit, sed ornare urna sapien nec ex. Vivamus orci metus, ornare eget dignissim non, accumsan vitae felis. Duis sit amet porta erat. Nullam venenatis vitae felis sit amet fermentum. Donec vestibulum at justo ac lacinia. Praesent euismod volutpat purus, id sodales mauris pulvinar non.

Integer eu pulvinar orci, vel tristique leo. Morbi elementum dui est, et consectetur mauris aliquet vitae. Integer gravida nisi vitae magna dignissim sodales. Nam varius metus nec lobortis euismod. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse cursus id turpis vitae ornare. Pellentesque risus ex, posuere nec sodales quis, sagittis sed ipsum. Morbi congue, ligula eu molestie condimentum, lorem risus hendrerit purus, vitae cursus massa arcu in arcu. Sed sem enim, dignissim ac dapibus sit amet, congue aliquet nisl. Suspendisse aliquam libero dolor, et facilisis metus auctor nec. Quisque id rhoncus enim. Praesent non lectus sit amet lectus aliquet pharetra. Donec tincidunt est sed tristique venenatis. Integer vulputate gravida sem, nec placerat orci commodo eu.

Praesent suscipit eros non ante efficitur, quis laoreet tortor semper. Pellentesque scelerisque nec augue at consequat. Donec facilisis, dolor eu ultricies placerat, nisi turpis tincidunt elit, vel pharetra turpis augue sed mi. Maecenas erat ipsum, imperdiet vitae eleifend nec, maximus ac quam. Morbi blandit lobortis libero, posuere tincidunt mi blandit et. Morbi vel nibh lacus. Aliquam luctus tincidunt nunc non auctor. Nullam bibendum nunc non viverra maximus. Maecenas a turpis eros. In ac odio quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Integer nulla lectus, porttitor id posuere eu, aliquet eu est. Pellentesque hendrerit volutpat dictum. Donec ullamcorper, tellus sollicitudin tincidunt posuere, erat nunc accumsan magna, eu porttitor sapien nunc sit amet tellus. Nullam euismod a lorem quis blandit. Nulla gravida erat id metus ornare, in pharetra mauris porttitor. Nullam feugiat ante eu mi scelerisque eleifend nec at tellus. Aliquam erat volutpat. Morbi massa tortor, euismod nec maximus quis, cursus non enim. Proin ac dui et diam finibus placerat in sed leo. Quisque laoreet tortor urna, eget laoreet eros porttitor vel.

In porttitor sagittis dui ac malesuada. Pellentesque semper felis in leo hendrerit tempus. Vivamus diam sapien, convallis id elementum in, sollicitudin et ipsum. Praesent quis elementum orci. Duis mauris mi, lobortis ac gravida nec, elementum ut nisi. Sed tempor sit amet purus vitae aliquet. Nullam et sodales erat.

Aenean ut urna sed justo hendrerit venenatis vitae et risus. Integer dictum gravida varius. Suspendisse ultricies aliquam tincidunt. Mauris sodales in mauris a viverra. Etiam bibendum leo sit amet ligula dapibus, a egestas nulla accumsan. Praesent id lacus ipsum. Donec turpis est, pellentesque nec felis a, pulvinar tincidunt nibh. Quisque vel vestibulum mauris. Nulla porta et arcu volutpat porta. Cras congue, dolor et vulputate egestas, ipsum risus rutrum odio, ac gravida nunc eros non orci. Proin ultrices orci eu efficitur sagittis. Proin rhoncus augue nec purus tempor blandit.

Quisque vel arcu iaculis, auctor massa at, imperdiet lacus. Nunc id bibendum arcu, sed bibendum mi. Integer id velit non ante laoreet lacinia. Nulla interdum et nibh eu scelerisque. Nam porttitor velit sollicitudin lectus vehicula sodales interdum et mi. Integer ut metus ultrices, porttitor lacus eget, vestibulum massa. Ut placerat, massa sit amet bibendum tempus, enim ante cursus augue, et fringilla purus lorem ut dui. Proin finibus vel libero eget porttitor. Vestibulum ut vehicula odio, at lacinia eros. Pellentesque iaculis sodales volutpat.

Donec auctor efficitur erat eu eleifend. Aenean sed tortor tellus. Sed fermentum, tortor quis tempus mattis, ligula ipsum eleifend nisl, non malesuada diam ipsum at sapien. Aliquam feugiat erat ac turpis volutpat sagittis. Nullam mattis nisi hendrerit, sodales turpis ut, egestas arcu. Curabitur semper turpis non elementum faucibus. Phasellus at elementum quam. Fusce egestas nisi metus, nec pretium nulla consectetur in. Proin congue suscipit sapien ut laoreet. Nam diam justo, pulvinar vitae sem eu, efficitur finibus libero. Vestibulum euismod mauris eu massa efficitur maximus. Praesent turpis nunc, facilisis quis rhoncus eu, sollicitudin vitae lectus. Nulla et tincidunt eros. Vivamus sit amet dignissim mi. Mauris luctus libero ipsum, id tristique ipsum mollis in. Pellentesque egestas tempus ipsum, ac consectetur nisl auctor sodales.

Suspendisse sem ante, volutpat ac feugiat quis, venenatis at neque. Proin fermentum est magna, ac suscipit erat vehicula in. Sed faucibus vitae enim quis fermentum. Cras vestibulum massa quis lacinia imperdiet. Duis id enim maximus, rutrum justo eu, sodales orci. Duis scelerisque facilisis tortor, quis varius risus dapibus at. Quisque molestie aliquam felis, sed placerat tellus dignissim eget. Proin consectetur, tellus at molestie iaculis, tellus arcu pharetra sem, nec placerat diam odio non nunc. Morbi gravida ligula porttitor, hendrerit nibh sit amet, bibendum ex. Quisque consectetur ultricies tortor, eget interdum nulla pellentesque at.

Aenean vitae euismod orci, eu porta justo. Nullam odio leo, tristique et dolor eu, suscipit efficitur nulla. Duis efficitur risus ligula, et laoreet urna aliquet ut. Nunc vel venenatis libero, vitae aliquet metus. Donec nec velit id velit vestibulum eleifend quis vel augue. Nulla euismod semper est in elementum. Integer auctor ex non nunc mollis, non pretium purus gravida. Sed suscipit eget risus nec suscipit. Interdum et malesuada fames ac ante ipsum primis in faucibus.

Fusce quis dolor sed dolor malesuada scelerisque id ut mauris. Donec egestas placerat tortor, nec feugiat lacus dictum ut. Maecenas sit amet viverra lacus, non sollicitudin diam. Praesent rhoncus libero ac mauris pulvinar gravida. Donec luctus massa risus, vestibulum dignissim sapien euismod ac. In volutpat nunc sit amet mauris cursus, sed iaculis erat ornare. Curabitur egestas euismod pellentesque. Aliquam quis ante eget nibh vehicula malesuada. Vestibulum tincidunt ex et metus pulvinar, sed facilisis augue pretium. Integer imperdiet commodo maximus. Aliquam lacinia pellentesque volutpat. Mauris eget dui eget nunc interdum accumsan quis sed purus. Donec nibh libero, eleifend nec est in, efficitur interdum leo. Curabitur semper justo nec tortor bibendum bibendum. Praesent eros mauris, accumsan eget gravida sed, feugiat nec purus. Etiam eu mi ut orci placerat efficitur nec sed mauris.

Quisque aliquam, dui quis egestas sagittis, massa est lacinia erat, non malesuada turpis elit dapibus erat. Donec sollicitudin, odio at vehicula varius, leo risus mattis quam, sed tempus purus arcu non nisi. Maecenas varius at nunc in mattis. Mauris commodo elit elit, eu fringilla nibh finibus vel. Vivamus posuere metus vitae odio consequat varius. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris porta orci non nisl rhoncus faucibus. Sed quam tortor, malesuada id fermentum a, accumsan in urna. Vestibulum pulvinar tellus justo. Quisque nec commodo libero. Sed non pellentesque elit. Suspendisse at scelerisque velit, a gravida tellus.

Pellentesque suscipit aliquam magna vitae facilisis. Donec volutpat ante a bibendum sodales. Donec interdum ante vitae erat molestie, at consequat ante viverra. Vivamus faucibus rutrum nisi nec venenatis. Sed nisi odio, pellentesque a finibus non, pretium non lorem. Aliquam condimentum tortor sit amet urna tincidunt, nec fermentum lacus pulvinar. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce varius ipsum nunc, at porttitor tellus semper ac. Sed vel maximus mi. Vestibulum non laoreet orci. Sed suscipit dui nulla, scelerisque egestas libero luctus non. Nullam vel sapien non velit ultrices condimentum ut sed sem. Integer tincidunt lacus tristique nulla lobortis blandit. Donec ligula neque, fringilla eu ex id, fermentum dictum tellus.

Nulla varius gravida tortor dapibus viverra. Nullam a leo libero. Morbi bibendum nibh orci, id luctus nisi sollicitudin at. Curabitur non nibh quis massa dapibus aliquet et a elit. Duis non nunc sapien. Ut sit amet dolor faucibus, laoreet mauris eget, viverra orci. Donec hendrerit purus sit amet elit sodales, in pharetra risus auctor. Donec feugiat, enim a egestas dictum, elit lectus eleifend dui, eu fermentum turpis tellus a ligula. Nunc sed luctus risus. Duis rutrum augue erat, ac ultricies nunc varius at. Nulla dapibus neque dictum arcu cursus mattis. Mauris in accumsan metus. Nulla et dolor enim. Aliquam eros lorem, ornare in semper at, pretium sed libero. Praesent ac fermentum est. Cras viverra metus quis massa placerat rhoncus.

Etiam placerat, sapien eget mollis mollis, tortor ligula pulvinar risus, ornare pretium lacus nisl sed nisi. Vestibulum mollis dolor eu ex dapibus pretium. Proin ut ultrices dui. Vivamus id metus placerat, aliquam lectus nec, scelerisque nisi. Donec facilisis risus sed pellentesque ullamcorper. Nulla ut consectetur lacus. Suspendisse scelerisque sapien vel dolor venenatis, sed commodo lacus lobortis. Suspendisse ac dolor magna. Aenean risus mauris, varius non dolor eget, sollicitudin ornare ex. Sed facilisis, arcu sit amet semper tristique, libero quam blandit lacus, nec elementum urna nibh eget odio. Donec sed augue augue. Nam a felis metus. Maecenas facilisis, enim sit amet ultricies aliquet, mi elit varius nisi, non bibendum augue arcu sed dui.

Sed vestibulum magna a lacinia vulputate. Integer tristique, nibh non pellentesque ullamcorper, enim enim efficitur neque, eget porta eros quam ac tellus. Ut feugiat massa eget massa eleifend, non bibendum diam volutpat. Nullam iaculis posuere tortor ut tempor. Nunc eu lacus vulputate, dapibus dolor nec, convallis nisi. Fusce accumsan risus ac est rutrum, sit amet porttitor nisl euismod. Donec venenatis risus in ipsum scelerisque, in scelerisque tortor eleifend. Phasellus ut magna sit amet velit porttitor euismod. Ut pharetra egestas posuere. Nulla fermentum, nisl tincidunt condimentum commodo, justo ante pulvinar nisi, in aliquam metus odio vel neque. Sed id tempor nibh. Nullam ac nisl pulvinar, pharetra eros eget, volutpat neque. Integer nulla felis, feugiat aliquam dolor ac, aliquam scelerisque felis.

Vestibulum odio felis, volutpat ut vestibulum vitae, fringilla sit amet est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras congue ut ipsum et consequat. Aenean orci mauris, pulvinar ut justo quis, vestibulum commodo lorem. Duis convallis efficitur turpis id condimentum. Etiam venenatis sed felis id consectetur. Aenean rutrum ornare arcu in efficitur. In at cursus orci. Aenean cursus ex lacus, sit amet faucibus leo vulputate sit amet. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

Ut accumsan nulla pharetra, tristique nisi et, congue nunc. Aliquam nisi nisi, rhoncus efficitur luctus malesuada, posuere a leo. Maecenas ultrices viverra ipsum sit amet viverra. Pellentesque vitae vehicula tortor, eget fermentum ipsum. Ut tempor congue lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et nulla ac ex rhoncus maximus. Duis diam nisl, rhoncus id nulla in, vulputate porta ex. Praesent blandit erat a vestibulum condimentum. Nulla commodo orci id sollicitudin facilisis. Curabitur eleifend ante orci, in maximus neque ullamcorper sit amet. Donec id pretium sem, eget aliquet urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin accumsan eros in euismod lacinia.

Fusce nisi est, interdum eu lectus nec, feugiat consectetur tellus. Donec hendrerit sodales mi quis mattis. Quisque ut nibh leo. Suspendisse facilisis varius risus vitae semper. Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur consequat arcu a nisi lacinia, nec efficitur justo fermentum. Nam ex elit, hendrerit vitae bibendum id, euismod in ligula. Morbi vel sollicitudin nibh. Quisque in magna condimentum, iaculis lectus et, lobortis libero. Duis molestie vehicula velit non molestie. Integer convallis ut ante a condimentum. Sed bibendum felis urna, quis rhoncus nulla sollicitudin venenatis. Morbi vel massa placerat, porttitor libero vitae, egestas ligula. Sed aliquet tortor sed hendrerit malesuada. Pellentesque tristique blandit risus quis laoreet. Etiam quis lectus diam.

Morbi laoreet mauris at augue volutpat viverra. Nulla risus lacus, vehicula dignissim dui in, sollicitudin pulvinar tortor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec id congue velit, ac elementum orci. Nam pretium porttitor convallis. Fusce vitae velit porta, interdum lorem eget, ornare mauris. Morbi nibh neque, sagittis ac porta blandit, egestas accumsan augue. Phasellus nec sem faucibus, feugiat magna ac, tincidunt elit. Maecenas vel sagittis sapien, et interdum odio. In malesuada, nulla ac porttitor scelerisque, risus eros pharetra libero, eget pellentesque elit dolor sed odio. Donec est dolor, scelerisque sit amet tristique non, hendrerit vitae ligula. Vivamus non mi et metus finibus faucibus vel vitae enim. Mauris non nunc volutpat, placerat dolor et, aliquet leo. Etiam rutrum interdum quam id maximus.

Cras sit amet luctus eros, eget tempus tortor. Proin suscipit eros ligula, non bibendum sem porttitor ac. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc condimentum a mi id luctus. Quisque ligula tellus, egestas sit amet iaculis consectetur, pellentesque sed nulla. Aenean porttitor tristique finibus. Aenean aliquam eleifend augue, eu consectetur orci euismod a. Vivamus suscipit elit sed sapien tristique sollicitudin eget in odio. Suspendisse aliquam odio eget nisl suscipit, nec venenatis eros aliquet. Nulla dictum nibh id mattis efficitur.

Donec faucibus tellus eget egestas maximus. Sed odio lacus, mattis quis mauris id, placerat hendrerit lorem. Pellentesque laoreet ipsum a orci faucibus imperdiet. Sed vel magna quis urna blandit porta vel luctus ligula. Fusce maximus convallis ipsum at pellentesque. Morbi mollis tincidunt interdum. Donec consectetur accumsan lectus et euismod. Proin tempus, felis commodo convallis vehicula, erat nisi sagittis mauris, et consectetur risus elit id erat. Aenean vel turpis in risus mollis faucibus. Etiam efficitur leo ac nunc eleifend, nec egestas risus ullamcorper. Cras elit felis, faucibus eget aliquet vel, varius accumsan nunc. Praesent auctor metus nibh, sed interdum leo tristique non. Phasellus dignissim libero vitae commodo porta. Donec nec ullamcorper ante.

Mauris et libero id massa dignissim euismod at non ligula. Vivamus quis pellentesque eros, vitae faucibus leo. Donec pretium luctus cursus. Fusce imperdiet est vel ex vestibulum convallis. In volutpat, mauris eget suscipit tristique, justo enim fringilla lorem, quis pellentesque elit ante a dui. Aliquam eget tincidunt justo. Nam vestibulum, libero non scelerisque dictum, libero mauris viverra purus, sit amet consequat felis lacus eget mauris. Nullam facilisis purus posuere, ultricies sapien vel, semper augue. Quisque ut molestie metus. Praesent felis nibh, auctor a ligula in, elementum blandit magna. Maecenas placerat tempus diam, quis pretium magna varius nec. Vestibulum rhoncus lacus in pharetra eleifend. Mauris vitae felis mauris. Curabitur eget nibh euismod magna suscipit imperdiet.

Ut a nulla ipsum. Ut vel risus rutrum, ornare nisi tincidunt, consectetur ante. Nam vel erat ac metus gravida fringilla a vitae ex. Sed euismod lectus vel sodales venenatis. Vivamus non pharetra lectus. Pellentesque ut justo vitae metus egestas aliquam. Praesent non justo ac nisi tempor pellentesque. In aliquet, urna vitae ultrices pellentesque, turpis leo luctus odio, luctus volutpat diam dolor sit amet lorem. Praesent accumsan urna id libero cursus, in laoreet dolor semper. Suspendisse potenti. In tempor sollicitudin dolor. Donec vel volutpat arcu. Aliquam erat volutpat. Nullam viverra finibus sem eget laoreet.

Proin sapien tellus, porttitor eu justo at, tristique rhoncus sapien. Duis in accumsan velit, ac rutrum justo. In sit amet gravida eros, ac congue mauris. Integer efficitur imperdiet magna, nec lacinia nulla tempor et. Praesent dui felis, volutpat sed aliquet elementum, molestie hendrerit nisl. Donec vitae ullamcorper massa. Quisque et cursus elit, nec rutrum nisi. Duis lacinia lacus in leo lobortis hendrerit. Donec a tincidunt justo. Nunc odio nibh, consequat eget varius non, porta ac metus. Nullam gravida massa et molestie dapibus. Morbi tristique justo eget risus lobortis dapibus. Phasellus aliquet lacus a congue facilisis.

Duis sodales eros vitae consectetur placerat. Nunc consequat interdum vehicula. Suspendisse potenti. Donec hendrerit leo vel quam laoreet dignissim. Fusce at est venenatis, interdum lacus et, scelerisque arcu. Suspendisse eget congue nisl. Curabitur tempus quam sit amet ipsum porta pretium. Integer venenatis et sem at porttitor.

Praesent ut lectus odio. Phasellus a lectus quis sem aliquet viverra sed sit amet mi. Phasellus eget mauris eget urna ornare pharetra sed sed libero. Sed in tempus leo. Sed id arcu placerat, ultrices est nec, aliquam quam. Donec porta, ante vel pulvinar sagittis, sem nisi maximus orci, condimentum tempor augue neque non lectus. Proin sed nibh eu dolor congue consequat at cursus leo.

Vestibulum scelerisque ipsum id dui tincidunt tempor ut et est. Nulla sollicitudin rutrum magna. Aliquam aliquet imperdiet massa id congue. Proin efficitur vel tellus vel porttitor. Integer iaculis risus ac sem elementum, vel facilisis nisl feugiat. Donec vel lacus quis turpis mattis ullamcorper nec vitae justo. Quisque eros arcu, imperdiet non rutrum non, elementum at massa. Quisque vel enim nec eros finibus sollicitudin. Maecenas non sagittis libero. Fusce ac hendrerit odio. Nunc mollis porttitor turpis, eu vehicula sem iaculis et. Integer nibh mi, sagittis quis nulla vitae, dapibus vulputate ante. Proin tincidunt lorem nisl, ut volutpat magna porttitor at. Ut vitae tincidunt metus, vitae mattis est.

Nunc id enim sed tortor congue commodo. Donec tincidunt felis id metus fringilla posuere. Integer eget finibus lectus. Sed egestas eros et eros pretium, non venenatis tellus facilisis. Nam vehicula diam et pulvinar lacinia. Sed elementum iaculis urna, vitae sodales mauris auctor ac. In dignissim lorem et porttitor faucibus. Fusce mattis turpis sed arcu faucibus pretium. Mauris diam neque, commodo quis elementum et, posuere et lorem. Suspendisse potenti. Nullam elementum justo et ipsum tristique blandit.

Proin accumsan nisl ac leo sollicitudin hendrerit. Maecenas quis vestibulum massa. Morbi ac nibh sit amet felis laoreet feugiat id sed ligula. Cras sed dui dapibus, scelerisque velit a, iaculis ligula. Sed dolor diam, consequat eget rhoncus ac, sagittis eget enim. Sed imperdiet velit sed risus ultricies venenatis. Aenean ut ipsum dolor. Nam dignissim ante consequat faucibus accumsan. Donec et volutpat justo. Mauris odio orci, cursus nec neque non, mattis porttitor purus. Nullam aliquam lorem in nisl pellentesque viverra. Vivamus quis pharetra neque, eu sollicitudin nunc. Praesent facilisis orci quis quam scelerisque iaculis. Aliquam erat volutpat.

Pellentesque vehicula viverra vestibulum. Etiam auctor sapien non quam imperdiet vehicula. Aliquam erat volutpat. Donec nulla nibh, blandit ac tortor vitae, consectetur dignissim elit. Curabitur sit amet vulputate dolor. Morbi vel maximus quam. Praesent id orci est. Aliquam sed fringilla enim. Proin sollicitudin finibus dolor, non ultrices ex sollicitudin at. Ut lobortis mollis lorem et blandit. Pellentesque interdum leo neque, sit amet commodo urna consectetur nec. Duis finibus est at elit pretium condimentum.

Integer fringilla iaculis mauris, ac placerat dui. Quisque urna magna, volutpat non ullamcorper ac, pharetra suscipit dolor. Nam laoreet a mauris nec ultricies. Mauris vitae leo justo. Aliquam et aliquam sapien. Mauris mollis lacinia sapien id venenatis. Duis ipsum ipsum, convallis convallis scelerisque in, facilisis laoreet nulla. Proin ornare metus ac lacinia interdum. Etiam dapibus ipsum molestie turpis porttitor, eu ultrices odio dapibus. Nunc vitae cursus turpis. Donec vel felis at turpis pretium semper non ut mauris. Nunc ultrices neque sed ullamcorper lacinia. Praesent non sem sed lorem egestas dapibus. Nullam blandit, augue a cursus faucibus, leo augue vulputate tortor, eu vehicula dolor elit sit amet augue.

Aenean at nunc vel lectus viverra dictum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse mattis in lacus non posuere. Etiam nec quam convallis ligula congue interdum sed nec eros. Suspendisse eget gravida ligula. Curabitur aliquam blandit sollicitudin. Integer accumsan elementum interdum. Sed elit enim, sagittis et urna quis, scelerisque volutpat ipsum. Nunc varius libero id leo volutpat, euismod convallis purus ornare. Phasellus lobortis volutpat erat. Vestibulum sit amet tellus eget nulla tristique placerat at ullamcorper justo. Quisque vitae leo rhoncus, luctus neque id, lacinia lorem. Sed sodales turpis non velit ultricies lobortis. Curabitur quis efficitur tortor. Donec commodo faucibus eleifend.

Ut odio libero, blandit id ullamcorper id, lobortis eget ex. Fusce aliquet tellus enim, porttitor tincidunt mi porttitor vel. Sed commodo lectus turpis, at pharetra ex hendrerit id. Suspendisse pretium leo vel sem sodales condimentum. Cras porta, nunc nec auctor ullamcorper, ligula turpis hendrerit tellus, ac condimentum diam urna sed turpis. Sed imperdiet pulvinar lacus, a bibendum magna ullamcorper eu. Aenean vulputate tempor sapien, et venenatis felis malesuada eu. Nulla gravida risus a lorem pretium imperdiet. Aliquam ultricies risus sed odio sollicitudin, iaculis rutrum lorem scelerisque. In porttitor lacus quam, at vehicula orci bibendum eu. Donec posuere eu neque non imperdiet. Maecenas eget vulputate justo. Pellentesque tortor urna, vulputate eget tellus eget, pharetra suscipit nibh. Fusce at ipsum eleifend nibh aliquam porta. Nam vitae justo scelerisque, posuere eros at, gravida orci. Donec sem risus, ullamcorper in aliquam nec, lobortis sed lacus.

Donec non ipsum sit amet mauris mattis tincidunt ut a leo. Quisque volutpat eget elit quis suscipit. Mauris id nulla varius, suscipit nulla vel, tincidunt augue. Nulla tristique augue diam, et malesuada tellus hendrerit a. Sed lobortis, nulla nec pulvinar tempus, est mi molestie urna, efficitur gravida metus odio ac eros. Sed at porttitor lectus, eget aliquam lectus. Proin at pretium diam. Phasellus commodo rutrum nisl, et maximus enim rutrum ac. Morbi magna ligula, elementum eget mauris eget, gravida molestie turpis.

Nunc gravida, lorem ut volutpat malesuada, neque mi sodales massa, ut malesuada erat leo eu nisi. Duis ac turpis nec risus ullamcorper suscipit. Duis quis ante gravida, hendrerit mauris quis, congue tellus. Suspendisse lacinia non nisl at gravida. Nam a mi turpis. Maecenas ac mollis nisi. Maecenas dolor magna, semper ac faucibus non, sollicitudin et nisi. Suspendisse ut sapien elit. Suspendisse commodo lacus in augue tempor ullamcorper. Proin euismod augue eu ipsum cursus fringilla. Nunc vitae tortor tellus.
    """,
]

class ConversationScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()

        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def resizeEvent(self, event):
        self.widget().setFixedWidth(event.size().width())
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    scroll = ConversationScrollArea()
    scroll_widget = QWidget()
    scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    scroll.setWidget(scroll_widget)
    scroll_widget_layout = QVBoxLayout()
    scroll_widget.setLayout(scroll_widget_layout)

    for i in range(len(strings)):
        bubble = QWidget()
        bubble.setStyleSheet("QLabel { background-color: #CFCFCF; }")
        bubble_layout = QHBoxLayout()
        bubble.setLayout(bubble_layout)
        label = QLabel()
        label.setWordWrap(True)
        label.setText(strings[i])
        bubble_layout.addWidget(label, stretch=2)
        bubble_layout.addWidget(QWidget(), stretch=1)
        scroll_widget_layout.addWidget(bubble)

    central_layout = QHBoxLayout()
    central_widget = QWidget()
    central_widget.setLayout(central_layout)
    central_layout.addWidget(scroll)
    central_layout.addStretch()

    w = QMainWindow()
    w.setCentralWidget(scroll)
    w.showMaximized()
    w.show()

    sys.exit(app.exec_())
