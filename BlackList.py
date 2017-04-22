from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.dictadapter import DictAdapter


# ----------------------------------------------------------------------------
# A dictionary of dicts, with only the minimum required is_selected attribute,
# for use with examples using a simple list of integers in a list view.
integers_dict = {str(i): {'text': str(i), 'is_selected': False}
                 for i in range(100)}

# ----------------------------------------------------------------------------
# A dataset of fruit category and fruit data for use in examples.
#
# Data from http://www.fda.gov/Food/LabelingNutrition/\
#                FoodLabelingGuidanceRegulatoryInformation/\
#                InformationforRestaurantsRetailEstablishments/\
#                ucm063482.htm
#
# Available items for import are:
#
#     fruit_categories
#     fruit_data_attributes
#     fruit_data_attribute_units
#     fruit_data_list_of_dicts
#     fruit_data
#
fruit_categories = {
    'Melons': {
        'name': 'Melons',
        'fruits': ['Cantaloupe', 'Honeydew', 'Watermelon'],
        'is_selected': False},
    'Tree Fruits': {
        'name': 'Tree Fruits',
        'fruits': ['Apple', 'Avocado', 'Banana', 'Nectarine', 'Peach', 'Pear',
                   'Pineapple', 'Plum', 'Cherry'],
        'is_selected': False},
    'Citrus Fruits': {
        'name': 'Citrus Fruits',
        'fruits': ['Grapefruit', 'Lemon', 'Lime', 'Orange', 'Tangerine'],
        'is_selected': False},
    'Other Fruits': {
        'name': 'Other Fruits',
        'fruits': ['Grape', 'Kiwifruit', 'Strawberry'],
        'is_selected': False}}

fruit_data_list_of_dicts = [
    {
        'name': 'Apple',
        'Serving Size': '1 large (242 g/8 oz)',
        'data': [130, 0, 0, 0, 0, 0, 260, 7, 34, 11, 5, 20, 25, 1, 2, 8, 2, 2],
        'is_selected': False},
    {
        'name': 'Avocado',
        'Serving Size': '1/5 medium (30 g/1.1 oz)',
        'data': [50, 35, 4.5, 7, 0, 0, 140, 4, 3, 1, 1, 4, 0, 1, 0, 4, 0, 2],
        'is_selected': False},
    {
        'name': 'Banana',
        'Serving Size': '1 medium (126 g/4.5 oz)',
        'data': [110, 0, 0, 0, 0, 0, 450, 13, 30, 10, 3, 12, 19,
                 1, 2, 15, 0, 2],
        'is_selected': False},
    {
        'name': 'Cantaloupe',
        'Serving Size': '1/4 medium (134 g/4.8 oz)',
        'data': [50, 0, 0, 0, 20, 1, 240, 7, 12, 4, 1, 4, 11, 1, 120,
                 80, 2, 2],
        'is_selected': False},
    {
        'name': 'Grapefruit',
        'Serving Size': '1/2 medium (154 g/5.5 oz)',
        'data': [60, 0, 0, 0, 0, 0, 160, 5, 15, 5, 2, 8, 11, 1, 35, 100, 4, 0],
        'is_selected': False},
    {
        'name': 'Grape',
        'Serving Size': '3/4 cup (126 g/4.5 oz)',
        'data': [90, 0, 0, 0, 15, 1, 240, 7, 23, 8, 1, 4, 20, 0, 0, 2, 2, 0],
        'is_selected': False},
    {
        'name': 'Honeydew',
        'Serving Size': '1/10 medium melon (134 g/4.8 oz)',
        'data': [50, 0, 0, 0, 30, 1, 210, 6, 12, 4, 1, 4, 11, 1, 2, 45, 2, 2],
        'is_selected': False},
    {
        'name': 'Kiwifruit',
        'Serving Size': '2 medium (148 g/5.3 oz)',
        'data': [90, 10, 1, 2, 0, 0, 450, 13, 20, 7, 4, 16, 13,
                 1, 2, 240, 4, 2],
        'is_selected': False},
    {
        'name': 'Lemon',
        'Serving Size': '1 medium (58 g/2.1 oz)',
        'data': [15, 0, 0, 0, 0, 0, 75, 2, 5, 2, 2, 8, 2, 0, 0, 40, 2, 0],
        'is_selected': False},
    {
        'name': 'Lime',
        'Serving Size': '1 medium (67 g/2.4 oz)',
        'data': [20, 0, 0, 0, 0, 0, 75, 2, 7, 2, 2, 8, 0, 0, 0, 35, 0, 0],
        'is_selected': False},
    {
        'name': 'Nectarine',
        'Serving Size': '1 medium (140 g/5.0 oz)',
        'data': [60, 5, 0.5, 1, 0, 0, 250, 7, 15, 5, 2, 8, 11, 1, 8, 15, 0, 2],
        'is_selected': False},
    {
        'name': 'Orange',
        'Serving Size': '1 medium (154 g/5.5 oz)',
        'data': [80, 0, 0, 0, 0, 0, 250, 7, 19, 6, 3, 12, 14, 1, 2, 130, 6, 0],
        'is_selected': False},
    {
        'name': 'Peach',
        'Serving Size': '1 medium (147 g/5.3 oz)',
        'data': [60, 0, 0.5, 1, 0, 0, 230, 7, 15, 5, 2, 8, 13, 1, 6, 15, 0, 2],
        'is_selected': False},
    {
        'name': 'Pear',
        'Serving Size': '1 medium (166 g/5.9 oz)',
        'data': [100, 0, 0, 0, 0, 0, 190, 5, 26, 9, 6, 24, 16, 1, 0, 10, 2, 0],
        'is_selected': False},
    {
        'name': 'Pineapple',
        'Serving Size': '2 slices, 3" diameter, 3/4" thick (112 g/4 oz)',
        'data': [50, 0, 0, 0, 10, 0, 120, 3, 13, 4, 1, 4, 10, 1, 2, 50, 2, 2],
        'is_selected': False},
    {
        'name': 'Plum',
        'Serving Size': '2 medium (151 g/5.4 oz)',
        'data': [70, 0, 0, 0, 0, 0, 230, 7, 19, 6, 2, 8, 16, 1, 8, 10, 0, 2],
        'is_selected': False},
    {
        'name': 'Strawberry',
        'Serving Size': '8 medium (147 g/5.3 oz)',
        'data': [50, 0, 0, 0, 0, 0, 170, 5, 11, 4, 2, 8, 8, 1, 0, 160, 2, 2],
        'is_selected': False},
    {
        'name': 'Cherry',
        'Serving Size': '21 cherries; 1 cup (140 g/5.0 oz)',
        'data': [100, 0, 0, 0, 0, 0, 350, 10, 26, 9, 1, 4, 16, 1, 2, 15, 2, 2],
        'is_selected': False},
    {
        'name': 'Tangerine',
        'Serving Size': '1 medium (109 g/3.9 oz)',
        'data': [50, 0, 0, 0, 0, 0, 160, 5, 13, 4, 2, 8, 9, 1, 6, 45, 4, 0],
        'is_selected': False},
    {
        'name': 'Watermelon',
        'Serving Size':
            '1/18 medium melon; 2 cups diced pieces (280 g/10.0 oz)',
        'data': [80, 0, 0, 0, 0, 0, 270, 8, 21, 7, 1, 4, 20, 1, 30, 25, 2, 4],
        'is_selected': False}]

fruit_data_attributes = ['(gram weight/ ounce weight)',
                         'Calories',
                         'Calories from Fat',
                         'Total Fat',
                         'Sodium',
                         'Potassium',
                         'Total Carbo-hydrate',
                         'Dietary Fiber',
                         'Sugars',
                         'Protein',
                         'Vitamin A',
                         'Vitamin C',
                         'Calcium',
                         'Iron']

fruit_data_attribute_units = ['(g)',
                              '(%DV)',
                              '(mg)',
                              '(%DV)',
                              '(mg)',
                              '(%DV)',
                              '(g)',
                              '(%DV)',
                              '(g)(%DV)',
                              '(g)',
                              '(g)',
                              '(%DV)',
                              '(%DV)',
                              '(%DV)',
                              '(%DV)']

attributes_and_units = dict(list(zip(fruit_data_attributes,
                                     fruit_data_attribute_units)))

fruit_data = {}
for fruit_record in fruit_data_list_of_dicts:
    fruit_data[fruit_record['name']] = {}
    fruit_data[fruit_record['name']] = \
            dict({'name': fruit_record['name'],
                  'Serving Size': fruit_record['Serving Size'],
                  'is_selected': fruit_record['is_selected']},
            **dict(list(zip(list(attributes_and_units.keys()),
                            fruit_record['data']))))

class FruitDetailView(GridLayout):
    fruit_name = StringProperty('', allownone=True)

    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        self.fruit_name = kwargs.get('fruit_name', '')
        super(FruitDetailView, self).__init__(**kwargs)
        if self.fruit_name:
            self.redraw()

    def redraw(self, *args):
        self.clear_widgets()
        if self.fruit_name:
            self.add_widget(Label(text="Name:", halign='right'))
            self.add_widget(Label(text=self.fruit_name))
            for attribute in fruit_data_attributes:
                self.add_widget(Label(text="{0}:".format(attribute),
                                      halign='right'))
                self.add_widget(
                    Label(text=str(fruit_data[self.fruit_name][attribute])))

    def fruit_changed(self, list_adapter, *args):
        if len(list_adapter.selection) == 0:
            self.fruit_name = None
        else:
            selected_object = list_adapter.selection[0]

            if type(selected_object) is str:
                self.fruit_name = selected_object
            else:
                self.fruit_name = selected_object.text

        self.redraw()

class MasterDetailView(GridLayout):
    '''Implementation of an master-detail view with a vertical scrollable list
    on the left (the master, or source list) and a detail view on the right.
    When selection changes in the master list, the content of the detail view
    is updated.
    '''

    def __init__(self, items, **kwargs):
        kwargs['cols'] = 2
        super(MasterDetailView, self).__init__(**kwargs)

        list_item_args_converter = \
                lambda row_index, rec: {'text': rec['name'],
                                        'size_hint_y': None,
                                        'height': 25}

        dict_adapter = DictAdapter(sorted_keys=sorted(fruit_data.keys()),
                                   data=fruit_data,
                                   args_converter=list_item_args_converter,
                                   selection_mode='single',
                                   allow_empty_selection=False,
                                   cls=ListItemButton)

        master_list_view = ListView(adapter=dict_adapter,
                                    size_hint=(.3, 1.0))

        self.add_widget(master_list_view)

        detail_view = FruitDetailView(
                fruit_name=dict_adapter.selection[0].text,
                size_hint=(.7, 1.0))

        dict_adapter.bind(on_selection_change=detail_view.fruit_changed)
        self.add_widget(detail_view)


if __name__ == '__main__':

    from kivy.base import runTouchApp

    master_detail = MasterDetailView(sorted(fruit_data.keys()), width=800)

    runTouchApp(master_detail)