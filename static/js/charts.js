var chart_data = {{ chart_data | safe }};
var chart_data_fac = {{ chart_data_fac | safe }};
var chart_data_haz = {{ chart_data_haz | safe }};
var ndx_data = crossfilter(chart_data);
var ndx_data_fac = crossfilter(chart_data_fac);
var ndx_data_haz = crossfilter(chart_data_haz);

// Defining dimensions of graph to match different screen sizes

function screenSize() {
    return  xxsmall.matches ? 300 :
            xsmall.matches ? 350 :
            small.matches ? 450 :
            small_medium.matches ? 240 :
            medium.matches ? 350 : 
            large.matches ? 400 :
            xlarge.matches ? 450 :
            null;
}

var xxsmall = window.matchMedia('(max-width: 350px)');
var xsmall = window.matchMedia('(max-width: 450px)');
var small = window.matchMedia('(max-width: 600px)');
var small_medium = window.matchMedia('(max-width: 800px)');
var medium = window.matchMedia('(max-width: 992px)');
var large = window.matchMedia('(max-width: 1199px)');
var xlarge = window.matchMedia('(min-width: 1200px)');
var width = screenSize();

function break_types_chart(ndx_data) {
    var name_dim = ndx_data.dimension(dc.pluck('break_type'));
    var break_types_per_loc = name_dim.group();
    dc.barChart('#break_types_per_loc')
        .width(width)
        .height(200)
        .margins({top: 10, right: 50, bottom: 40, left: 30})
        .dimension(name_dim)
        .group(break_types_per_loc)
        .transitionDuration(1500)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .xAxisLabel('Break Type')
        .yAxisLabel('Locations')
        .yAxis().ticks(4);
}

function bottom_chart(ndx_data) {
    var name_dim = ndx_data.dimension(dc.pluck('bottom'));
    var bottoms_per_loc = name_dim.group();
    dc.barChart('#bottoms_per_loc')
        .width(width)
        .height(200)
        .margins({top: 10, right: 50, bottom: 40, left: 30})
        .dimension(name_dim)
        .group(bottoms_per_loc)
        .transitionDuration(1500)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .xAxisLabel('Bottom Type')
        .yAxisLabel('Locations')
        .yAxis().ticks(4);
}

function facilities_chart(ndx_data_fac) {
    var name_dim = ndx_data_fac.dimension(dc.pluck('facilities'));
    var facilities_per_loc = name_dim.group();
    dc.pieChart("#facilities_per_loc")
        .height(400)
        .width(width + 50)
        .radius(90)
        .innerRadius(45)
        .transitionDuration(1500)
        .dimension(name_dim)
        .group(facilities_per_loc)
        .legend(dc.legend())
        .externalLabels(.8);
}

function hazards_chart(ndx_data_haz) {
    var name_dim = ndx_data_haz.dimension(dc.pluck('hazards'));
    var hazards_per_loc = name_dim.group();
    dc.pieChart("#hazards_per_loc")
        .height(400)
        .width(width + 50)
        .radius(90)
        .innerRadius(45)
        .transitionDuration(1500)
        .dimension(name_dim)
        .group(hazards_per_loc)
        .legend(dc.legend())
        .externalLabels(.8)
        .minAngleForLabel(.5);
}

break_types_chart(ndx_data);
bottom_chart(ndx_data);
facilities_chart(ndx_data_fac);
hazards_chart(ndx_data_haz);

dc.renderAll();