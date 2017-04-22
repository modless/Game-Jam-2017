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
#     drug_data_types
#     drug_data_attribute_units
#     drug_data_list_of_dicts
#     drug_data

drug_data_list_of_dicts = [
    {
        'name': 'Moskow',
        'Serving Size': '1 large (242 g/8 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Amsterdam',
        'Serving Size': '1/5 medium (30 g/1.1 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Melbourne',
        'Serving Size': '1 medium (126 g/4.5 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Dzakarta',
        'Serving Size': '1/4 medium (134 g/4.8 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Tokyo',
        'Serving Size': '1/2 medium (154 g/5.5 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Kyoto',
        'Serving Size': '3/4 cup (126 g/4.5 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Seoul',
        'Serving Size': '1/10 medium melon (134 g/4.8 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Shanghai',
        'Serving Size': '2 medium (148 g/5.3 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Bankok',
        'Serving Size': '1 medium (58 g/2.1 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Hyderabado',
        'Serving Size': '1 medium (67 g/2.4 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Islamabad',
        'Serving Size': '1 medium (140 g/5.0 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Kinshasa',
        'Serving Size': '1 medium (154 g/5.5 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Egypt',
        'Serving Size': '1 medium (147 g/5.3 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Ankara',
        'Serving Size': '1 medium (166 g/5.9 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Hamburg',
        'Serving Size': '2 slices, 3" diameter, 3/4" thick (112 g/4 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'London',
        'Serving Size': '2 medium (151 g/5.4 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Rio De Janeiro',
        'Serving Size': '8 medium (147 g/5.3 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Bogota',
        'Serving Size': '21 cherries; 1 cup (140 g/5.0 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Mexico',
        'Serving Size': '1 medium (109 g/3.9 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False},
    {
        'name': 'Chicago',
        'Serving Size':
            '1/18 medium melon; 2 cups diced pieces (280 g/10.0 oz)',
        'data': [1000, 2000, 3000, 7000, 2500, 1500, 6000, 3500, 5000, 26000, 2000, 14000, 2500, 30, 25, 2, 4],
        'is_selected': False}]

drug_data_types = ['Marijuana',
                         'Shrooms',
                         'LSD',
                         'Amphetamine',
                         'Cocaine',
                         'Crack',
                         'Ketamine',
                         'Ecstasy',
                         'Heroin',
                         'Kindey',
                         'Steroids',
                         'Hearth',
                         'Small intestine']

drug_data_attribute_units = ['(g)',
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

attributes_and_units = dict(list(zip(drug_data_types,
                                     drug_data_attribute_units)))

drug_data = {}
for drug_record in drug_data_list_of_dicts:
    drug_data[drug_record['name']] = {}
    drug_data[drug_record['name']] = \
            dict({'name': drug_record['name'],
                  'Serving Size': drug_record['Serving Size'],
                  'is_selected': drug_record['is_selected']},
            **dict(list(zip(list(attributes_and_units.keys()),
                            drug_record['data']))))

class DrugDetailView(GridLayout):
    drug_name = StringProperty('', allownone=True)

    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        self.drug_name = kwargs.get('drug_name', '')
        super(DrugDetailView, self).__init__(**kwargs)
        if self.drug_name:
            self.redraw()

    def redraw(self, *args):
        self.clear_widgets()
        if self.drug_name:
            self.add_widget(Label(text="Name:", halign='right'))
            self.add_widget(Label(text=self.drug_name))
            for attribute in drug_data_types:
                self.add_widget(Label(text="{0}:".format(attribute),
                                      halign='right'))
                self.add_widget(
                    Label(text=str(drug_data[self.drug_name][attribute])))

    def drug_changed(self, list_adapter, *args):
        if len(list_adapter.selection) == 0:
            self.drug_name = None
        else:
            selected_object = list_adapter.selection[0]

            if type(selected_object) is str:
                self.drug_name = selected_object
            else:
                self.drug_name = selected_object.text

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

        dict_adapter = DictAdapter(sorted_keys=sorted(drug_data.keys()),
                                   data=drug_data,
                                   args_converter=list_item_args_converter,
                                   selection_mode='single',
                                   allow_empty_selection=False,
                                   cls=ListItemButton)

        master_list_view = ListView(adapter=dict_adapter,
                                    size_hint=(.3, 1.0))

        self.add_widget(master_list_view)

        detail_view = DrugDetailView(
                drug_name=dict_adapter.selection[0].text,
                size_hint=(.7, 1.0))

        dict_adapter.bind(on_selection_change=detail_view.drug_changed)
        self.add_widget(detail_view)


if __name__ == '__main__':

    from kivy.base import runTouchApp

    master_detail = MasterDetailView(sorted(drug_data.keys()), width=800)

    runTouchApp(master_detail)