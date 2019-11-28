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
// chart.colors.list = [
//     am4core.color("#845EC2"),
//     am4core.color("#D65DB1"),
//     am4core.color("#FF6F91"),
//     am4core.color("#FF9671"),
//     am4core.color("#FFC75F"),
//     am4core.color("#F9F871"),
//   ];

series.dataFields.word = "value";
series.dataFields.value = "tagsize";


// series.heatRules.push({
//  "target": series.labels.template,
//  "property": "fill",
//  "min": am4core.color("#0000CC"),
//  "max": am4core.color("#CC00CC"),
//  "dataField": "value"
// });

// series.labels.template.url = "https://stackoverflow.com/questions/tagged/{word}";
// series.labels.template.urlTarget = "_blank";
series.labels.template.tooltipText = "{word}: {value}";

let hoverState = series.labels.template.states.create("hover");
hoverState.properties.fill = am4core.color("#FF0000");
