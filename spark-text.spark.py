import org.warcbase.spark.matchbox.ArcRecords
import org.warcbase.spark.matchbox.ArcRecords._

val r = ArcRecords.load("/Users/ianmilligan1/dropbox/warcs-workshop", sc)
  .keepMimeTypes(Set("text/html"))
  .discardDate(null)
  .keepDomains(Set("greenparty.ca"))
  .extractUrlAndBody()
r.saveAsTextFile("/Users/ianmilligan1/dropbox/output-live1")