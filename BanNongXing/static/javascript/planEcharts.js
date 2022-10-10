/*let map = document.querySelector(".territory_map_wrap")
let mapChart = echarts.init(map)
echarts.registerMap('china', mapData)
const initOption = {
  title: {
    text: '中国地图',
    left: 20,
    top: 20
  },
  legend: {
    left: '5%',
    bottom: '5%',
    orient: 'vertical' // 垂直摆放图例
  },
  geo: {
    type: 'map',
    map: 'china',
    top: '5%',
    bottom: '5%',
    itemStyle: {
      areaColor: '#2E72BF',
      borderColor: '#333'
    }
  }
}
this.chartInstance.setOption(initOption)

map.addEventListener('click', async arg => {
  // console.log(arg)
  const provinceInfo = getProvinceMapInfo(arg.name)
  // console.log(provinceInfo)
  // 获取该省份的地图矢量数据
  // 判断当前省份的地图矢量数据是否存在,不存在再发起请求

  // const { data: res } = await axios.get('http://localhost:8999' + provinceInfo.path)

  // 对省份矢量数据进行缓存
  this.mapData[provinceInfo.key] = res
  // console.log(res)
  mapChart.registerMap(provinceInfo.key, res)
  // console.log(this.mapData[provinceInfo.key])
  const changeOption = {
    geo: {
      map: provinceInfo.key
    }
  }
  mapChart.setOption(changeOption)
})*/


var myChart = echarts.init(document.querySelector('#plan_chart'), 'customed')
var pieData = [
  {
    value: 18,
    name: "钙",
  },
  {
    value: 12,
    name: "镁"
  },
  {
    value: 123,
    name: "钾"
  },
  {
    value: 64,
    name: "磷"
  },
  {
    value: 213,
    name: "氮"
  }
]
legendData = pieData.map(item => item.name)
var option = {
  title: {
    text: '单位：mg/kg',
    left: '10',
    textStyle: {
      color: '#A1A1A1',
      fontWeight: 'normal'
    }
  },
  legend: {
    data: legendData,
    icon: 'circle',
    top: '35%',
    right: '10%',
    orient: 'vertical',
  },
  tooltip: {
    trigger: 'item'
  },
  series: [
    {
      type: 'pie',
      data: pieData,
      radius: ['55%', '70%'],
      selectedMode: 'multiple',       // 选中模式
      selectedOffset: 30,             // 选中后偏移
      label: {
        show: true,
        formatter: function (arg) {
          return arg.data.name + ' ' + arg.data.value
        },
      },
    }
  ]
}
myChart.setOption(option)

