# -*- encoding: utf-8 -*-
##############################################################################
#
#    Web - Custom Search Quantity module for Odoo
#    Copyright (C) 2015-Today Akretion (http://www.akretion.com)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Web - Custom Search Quantity',
    'version': '1.0',
    'category': 'web',
    'description': """
Allow users to set manually a quantity of items to display in a tree view
=========================================================================

Functionality:
--------------
    * By default, in Odoo, user can display 80 / 200 / 500 / 2000 elements in
    a tree view;
    With that module, user can select a custom number of items to display;

Technical information:
----------------------
    * replace a select element by an input with datalist option. That allows
      to set a custom value, or to select an option. (same options as before:
      80 / 200 / 500 / 2000 / unlimited);

    * WARNING: 'Datalist' is a HTML5 tag; If your browser is not HTML5
      compliant, the options will not be displayed (but it is possible for
      user to select manually a value);
      See browser Support: http://www.w3schools.com/tags/tag_datalist.asp

Copyright, Author and Licence:
------------------------------
    * Copyright:
        * 2015-Today, Akretion;
    * Author:
        * Sylvain LE GAL (https://twitter.com/legalsylvain);
    * Licence: AGPL-3 (http://www.gnu.org/licenses/)""",
    'author': "GRAP,Odoo Community Association (OCA)",
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'web',
    ],
    'js': [
        'static/src/js/web_custom_search_quantity.js',
    ],
    'css': [
        "static/src/css/web_custom_search_quantity.css",
    ],
}
