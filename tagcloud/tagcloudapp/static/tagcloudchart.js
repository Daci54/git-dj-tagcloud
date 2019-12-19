/* Chart code */
// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end

function tagreplacer(tagsdata) {
    series.data = tagsdata;
}

let chart = am4core.create("chartdiv", am4plugins_wordCloud.WordCloud);
chart.fontFamily = "Arial";
let series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
series.randomness = 0.1;
series.accuracy = 5;
series.rotationThreshold = 0;

series.data;

series.colors = new am4core.ColorSet();

series.dataFields.word = "value";
series.dataFields.value = "tagsize";

series.heatRules.push({
 "target": series.labels.template,
 "property": "fill",
 "min": am4core.color("#0000CC"),
 "max": am4core.color("#CC00CC"),
 "dataField": "value"
});

series.labels.template.tooltipText = "{word}: Gewichtung {value}";

let hoverState = series.labels.template.states.create("hover");
hoverState.properties.fill = am4core.color("#FF0000");
