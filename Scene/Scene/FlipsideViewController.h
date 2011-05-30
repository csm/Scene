//
//  FlipsideViewController.h
//  Scene
//
//  Created by Casey Marshall on 5/28/11.
//  Copyright 2011 Modal Domains. All rights reserved.
//

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
