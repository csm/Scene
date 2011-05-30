//
//  FlipsideViewController.h
//  Scene
//
//  Created by Casey Marshall on 5/28/11.
//  Copyright 2011 Modal Domains. All rights reserved.
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#import <UIKit/UIKit.h>
#import "GradientButton.h"

@protocol FlipsideViewControllerDelegate;

@interface FlipsideViewController : UIViewController
{
    IBOutlet UILabel *locLabel;
    IBOutlet UILabel *locStatusLabel;
    IBOutlet UILabel *locServLabel;
    IBOutlet UILabel *accountLabel;
    IBOutlet UILabel *accountInsLabel;
    IBOutlet UITextField *nameField;
    IBOutlet UILabel *versionLabel;
    IBOutlet UILabel *copyrightLabel;
    IBOutlet GradientButton *button;
}

@property (nonatomic, assign) id <FlipsideViewControllerDelegate> delegate;

- (IBAction)done:(id)sender;

@end


@protocol FlipsideViewControllerDelegate
- (void)flipsideViewControllerDidFinish:(FlipsideViewController *)controller;
@end
